import requests
import json
import streamlit as st
import hashlib
import defSessionState as ss

import answer_qa
import model_add
import home
import list_qa
import list_models
import qa_file_uploader

st.set_page_config(
    # Can be "centered" or "wide". In the future also "dashboard", etc.
    layout="centered",
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    # String or None. Strings get appended with "• Streamlit".
    page_title="AM Transformers - Question Answering",
    page_icon=None,  # String, anything supported by st.image, or None.
)

PAGES = {
    "Home": home,
    "List Models": list_models,
    "Add New or Delete Models": model_add,
    "Ask a Question": answer_qa,
    "List Recently Answered Questions": list_qa,
    "Upload a File with Question & Context":qa_file_uploader
}

st.title("AM Transformers QA - Oracle")

def main():
    state = ss._get_state()
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    
    page = PAGES[selection].write(state)

    st.sidebar.title("About")
    st.sidebar.info(
            """
            Part of this app is maintained by Mr. Ayush Maheshwari.
            """)
    state.sync()
if __name__ == "__main__":
    main()
