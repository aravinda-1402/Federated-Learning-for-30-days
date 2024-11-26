import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the trained model
model = T5ForConditionalGeneration.from_pretrained("t5-small")
model.load_state_dict(torch.load("global_model.pth"))
tokenizer = T5Tokenizer.from_pretrained("t5-small")

st.title("Federated Text Summarizer")
st.write("Summarize text using a model trained with Federated Learning.")

# Text input
user_input = st.text_area("Enter text to summarize", height=200)

if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        inputs = tokenizer(user_input, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(inputs.input_ids, max_length=50, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.success(summary)
