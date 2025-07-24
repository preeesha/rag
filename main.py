import streamlit as st
from pages.custom_style import STYLING
st.set_page_config( 
    page_title="CodeGraph AI", page_icon="🕸️",
    layout="wide", initial_sidebar_state="expanded"
)
st.markdown(STYLING, unsafe_allow_html=True)
home_page = st.Page("pages/home.py", title="Home", icon = ":material/home:", default=True)
query = st.Page("pages/query.py", title="Query Tool", icon=":material/dashboard:")

pg = st.navigation( 
    {
        "MENU": [home_page, query]
    }
)
pg.run()