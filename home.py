import requests
import json
import streamlit as st

def write(state):
    st.markdown('')
    st.markdown('')
    st.title('Welcome to AM''s Transformers QA Web App')
    st.markdown('')
    st.subheader("Please use the sidebar to navigate through the different options in the application")
    st.markdown('''
        - Home - Landing Page for the Application  
        - List Models - This page will list all the transformers models loaded in the API
        - Add/Delete Models - This page will add and delete transformers QA models in the API
        - Answer your Question - This page will take a question and context and return the answer to the question
        - List Recently Answered Questions - This page will list all the recently answered questions
    ''')