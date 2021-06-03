import requests
import json
import streamlit as st
import os
import pandas as pd

def write(state):


    url = format(os.environ.get('API_URL'))
    url = url+'models'
    
    with try_expander('Add/Delete Models', False):
        if st.checkbox('Add Transformers QA Model', value=False):
            model_name =st.text_input('Model Name')
            model =st.text_input('Model')
            tokenizer = st.text_input('Tokenizer')
            if st.button('Add Model'):
                if (model_name!="" and model!="" and tokenizer!=""):
                    payload=json.dumps(
                    {
                    "name":model_name,
                    "model":model,
                    "tokenizer":tokenizer
                    })  
                    headers={'Content-Type':'application/json'}
                    response = requests.request("PUT", url, headers=headers, data=payload)              
                    data = json.loads(response.text)
                    output_pd = pd.DataFrame(data)
                    st.table(output_pd)
                else:
                    st.error('Always enter the Model Name, Model and Tokenizer Value')
    
        if st.checkbox('Delete Transformers QA Model', value=False):
            model_name_del = st.text_input('Model Name')
            if st.button('Delete Model'):
                if (model_name_del != ""):
                    delete_cmd = "?model="
                    url_del = url+delete_cmd+model_name_del
                    payload={}
                    headers = {}
                    response = requests.request("DELETE", url_del, headers=headers, data=payload)
                    data = json.loads(response.text)
                    output_pd = pd.DataFrame(data)
                    st.table(output_pd)
                else:
                    st.error('Model Name cannot be left empty')

def try_expander(expander_name, sidebar=True):
    if sidebar:
        try:
            return st.sidebar.expander(expander_name)
        except:
            return st.sidebar.beta_expander(expander_name)
    else:
        try:
            return st.expander(expander_name)
        except:
            return st.beta_expander(expander_name)  
