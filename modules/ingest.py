from langchain_community.document_loaders import WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def ingest_wikipedia_topic(topic: str):
    try:
        print("fetchning doc")
        loader = WikipediaLoader(query=topic, lang="en", load_max_docs=1)
        docs = loader.load()
        print(f"✅ Fetched {len(docs)} docs")
        
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

    

  
