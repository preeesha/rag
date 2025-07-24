from langchain_community.document_loaders import WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import time


def ingest_wikipedia_topic(topic: str):
    try:
        print(topic)
        print("fetchning doc")
        start = time.time()
        loader = WikipediaLoader(query=topic, lang="en", load_max_docs=1)
        docs = loader.load()
        print(docs)
        print(f"✅ Fetched {len(docs)} docs in {time.time() - start:.2f}s")
        
        try:
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_documents(docs)
            print(f"✅ Split {len(chunks)} chunks")
            
            try: 
                
                embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="./vectorstore")
                db.persist()
                print(f"✅ Stored '{topic}' into vectorstore.")
                
            except Exception as e:
                print(f"Error creating vectorstore: {e}")
                return
                
        except Exception as e:
            print(f"Error splitting docs: {e}")
            return
        
        
    except Exception as e:
        print(f"Error fetching docs: {e}")
        return


  

if __name__ == "__main__":
    ingest_wikipedia_topic("mughal empire")