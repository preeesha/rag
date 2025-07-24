from modules.query import query_from_db
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os

from modules.constants.constants import GOOGLE_API_KEY

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


query = ""


def rag_pipeline(query: str):
    try:
        prompt_template = ChatPromptTemplate(
            [
                (
                    "system",
                    "You are a helpful assistant that answers questions according to the context provided:{context}",
                ),
                ("user", "{query}"),
            ]
        )
        context = query_from_db(query)
        
        if not context:
            return "❌ No relevant context found. Please make sure you have ingested data first."
        
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)
        
        chain = prompt_template | llm | StrOutputParser()

        result = chain.invoke({"context": context, "query": query})
        
        return result
        
    except Exception as e:
        return f"❌ Error: {str(e)}"
    
if __name__ == "__main__":
    result = rag_pipeline("what is mughal empire?")
    print(result)
