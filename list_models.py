import requests
import json
import streamlit as st
import os
import pandas as pd

def write(state): 
    url = format(os.environ.get('API_URL'))
    url = url+'models'
    headers={}
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    output_pd = pd.DataFrame(data)
    st.table(output_pd)
