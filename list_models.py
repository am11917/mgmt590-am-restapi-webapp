import requests
import json
import streamlit as st

def write(state): 
    url = "https://mgmt590-am-rest-api-wbv4eowlaa-uc.a.run.app/models"
    headers={}
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    st.json(response.text)