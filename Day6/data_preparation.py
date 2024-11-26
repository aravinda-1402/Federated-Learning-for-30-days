from datasets import load_dataset

def prepare_datasets():
    """Download and prepare the CNN/DailyMail dataset."""
    dataset = load_dataset("cnn_dailymail", "3.0.0")
    print("Dataset Loaded:", dataset)

    num_clients = 3
    clients_data = {}

    # Dynamically calculate split sizes for each dataset
    for split in ["train", "validation"]:
        split_size = len(dataset[split])
        data_per_client = split_size // num_clients

        for i in range(num_clients):
            start_idx = i * data_per_client
            # Ensure we don't exceed the dataset size
            end_idx = min((i + 1) * data_per_client, split_size)

            if f"client_{i+1}" not in clients_data:
                clients_data[f"client_{i+1}"] = {}

            # Assign split data to clients
            clients_data[f"client_{i+1}"][split] = dataset[split].select(range(start_idx, end_idx))

            # Debug: Check the size of the assigned data
            print(f"Client {i+1} {split} Data Size: {len(clients_data[f'client_{i+1}'][split])}")

    return clients_data

if __name__ == "__main__":
    clients_data = prepare_datasets()
    print("Prepared datasets for clients.")
