import streamlit as st
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
from modules.ingest import ingest_wikipedia_topic

# Load environment variables
load_dotenv()

HUGGING_FACE_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "google/flan-t5-base"  # or "google/flan-t5-small" for smaller one




# Streamlit UI
st.title("🧠 Wikipedia RAG Chatbot")
st.markdown("Ask anything from the stored Wikipedia topic!")
topic = st.text_input("Enter the topic to search")
submit_button = st.button("Submit")

if submit_button:
    if topic:
        ingest_wikipedia_topic(topic)
        st.write("✅ Vectorstore created successfully!")
    else:
        st.error("Please enter a topic to search")
