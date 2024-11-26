import torch
import torch.nn as nn
from datasets import load_dataset
import torch.optim as optim
from transformers import T5Tokenizer, T5ForConditionalGeneration
from data_preparation import prepare_datasets
from tqdm import tqdm  # Progress bar library

# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("t5-small")
global_model = T5ForConditionalGeneration.from_pretrained("t5-small")

def train_client(data, model, epochs=2):
    """Train model on a single client's data."""
    optimizer = optim.Adam(model.parameters(), lr=5e-5)
    
    with tqdm(total=len(data) * epochs, desc="Training Client") as pbar:
        for epoch in range(epochs):
            for example in data:
                # Ensure example is a dictionary
                if not isinstance(example, dict):
                    print(f"Skipping invalid example: {example}")
                    pbar.update(1)
                    continue

                text = example.get("article", "")
                summary = example.get("highlights", "")

                if not text or not summary:
                    print(f"Skipping example with missing fields: {example}")
                    pbar.update(1)
                    continue

                inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
                labels = tokenizer(summary, return_tensors="pt", max_length=512, truncation=True)

                outputs = model(input_ids=inputs.input_ids, labels=labels.input_ids)
                loss = outputs.loss

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                # Update progress bar
                pbar.update(1)
    return model

def federated_averaging(global_model, clients_data, rounds=3):
    """Perform Federated Averaging across clients."""
    for rnd in tqdm(range(rounds), desc="Federated Rounds"):
        client_models = []

        for client_id, client_data in tqdm(clients_data.items(), desc=f"Round {rnd + 1} Clients"):
            print(f"Training on {client_id}")
            client_model = T5ForConditionalGeneration.from_pretrained("t5-small")
            client_model.load_state_dict(global_model.state_dict())  # Initialize with global model

            train_data = client_data["train"]
            client_model = train_client(train_data, client_model)
            client_models.append(client_model.state_dict())

        # Average model weights
        avg_weights = {}
        for key in global_model.state_dict().keys():
            avg_weights[key] = sum([model[key] for model in client_models]) / len(client_models)

        global_model.load_state_dict(avg_weights)  # Update global model

    return global_model

if __name__ == "__main__":
    # Prepare datasets
    clients_data = prepare_datasets()
    print("Debugging Example: ")
    print(clients_data["client_1"]["train"][0])

    # Perform federated training
    global_model = federated_averaging(global_model, clients_data)
    torch.save(global_model.state_dict(), "global_model.pth")
    print("Federated training completed and model saved.")
