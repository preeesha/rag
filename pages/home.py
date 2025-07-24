import streamlit as st
from modules.ingest import ingest_wikipedia_topic

st.title("ingestion page")
st.write("enter the topic you want to search on wikipedia and click on submit")
topic=st.text_input("enter the topic")
submit_button=st.button("submit")

if submit_button and topic:
    with st.spinner("processing..."):
        ingest_wikipedia_topic(topic)
        st.write("✅ vectorstore created successfully!")
else:
    st.error("please enter a topic to search")