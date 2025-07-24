from modules.llm import rag_pipeline
import streamlit as st

st.title("query page")
query=st.text_input("enter the query")
submit_button=st.button("submit")

if submit_button and query:
    with st.spinner("processing..."):
        result=rag_pipeline(query)
        st.write(result)