import requests
import json
import streamlit as st

def write(state): 
    url = format(os.environ.get('API_URL'))
    url = url+'models'
    headers={}
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    st.json(response.text)
