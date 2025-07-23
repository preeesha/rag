# Wikipedia RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that uses Wikipedia data and HuggingFace models.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up Environment Variables
1. Get your HuggingFace API token from: https://huggingface.co/settings/tokens
2. Create a `.env` file in the project root:
```bash
cp env_example.txt .env
```
3. Edit `.env` and add your HuggingFace token:
```
HUGGINGFACE_API_TOKEN=your_actual_token_here
```

### 3. Run Setup Script
```bash
python setup.py
```
This will:
- Check for required environment variables
- Ingest Wikipedia data about "artificial intelligence" (if no vectorstore exists)
- Create the vectorstore for the RAG system

### 4. Run the Application
```bash
streamlit run main.py
```

## 📁 Project Structure

```
rag/
├── main.py              # Streamlit application
├── setup.py             # Setup script
├── requirements.txt     # Python dependencies
├── modules/
│   └── ingest.py       # Data ingestion script
├── vectorstore/         # Chroma vector database
└── .env                 # Environment variables (create this)
```

## 🔧 Customization

### Change the Wikipedia Topic
Edit `setup.py` and modify the `topic` variable:
```python
topic = "your_topic_here"  # e.g., "machine learning", "python programming"
```

### Use Different Models
Edit `main.py` and change the model constants:
```python
HUGGING_FACE_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # Embeddings
LLM_MODEL = "google/flan-t5-base"  # Language model
```

## 🛠️ Troubleshooting

### "Vectorstore not found" Error
Run the setup script: `python setup.py`

### "HUGGINGFACE_API_TOKEN not found" Error
1. Create a `.env` file
2. Add your HuggingFace token
3. Restart the application

### "Error loading LLM" Error
- Check your HuggingFace token is valid
- Ensure you have internet connection
- Try a different model in `main.py`

## 📚 How it Works

1. **Data Ingestion**: Wikipedia articles are fetched and split into chunks
2. **Vectorization**: Text chunks are converted to embeddings using sentence-transformers
3. **Storage**: Embeddings are stored in a Chroma vector database
4. **Retrieval**: When you ask a question, similar chunks are retrieved
5. **Generation**: The LLM generates answers based on retrieved context 