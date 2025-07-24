from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


def query_from_db(query: str, k: int = 3) -> str:
    
    print(query)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = Chroma(persist_directory="./vectorstore", embedding_function=embeddings)

    print(f"Total documents in vectorstore: {db._collection.count()}")
    print(f"Collection name: {db._collection.name}")

    if db._collection.count() == 0:
        print("❌ Vectorstore is empty! You need to ingest data first.")
        print("Run: python main.py and enter a topic, or run: python modules/ingest.py")
        return ""

    results = db.similarity_search(query, k=k)
    
    context = ""
    if results:
        for result in results:
            context += result.page_content
            context += "\n"
        return context
    else:
        print("No results found for the query.")
        return ""

# if __name__ == "__main__":
#     query_from_db("Who was Babur?")
