import requests
import json
import streamlit as st
import os
import pandas as pd

def write(state):
 
    model_get_url = format(os.environ.get('API_URL'))
    model_get_url = model_get_url+'models'
    url = format(os.environ.get('API_URL'))
    url = url+'answer'
    headers={}
    payload={}
    response = requests.request("GET", model_get_url, headers=headers, data=payload)
    data = json.loads(response.text)
    output_pd = pd.DataFrame(data)
    model = st.selectbox("Select Model", options = output_pd['name'])
    question =st.text_input('Question')
    context =st.text_input('Context')
    
    if st.button('Answer button'):
        if (question != "" and context !=""):
            if(model == ""):
                payload=json.dumps(
                {
                "question":question,
                "context":context
                })  
                headers={'Content-Type':'application/json'}
                response = requests.request("POST", url, headers=headers, data=payload)
                answer = response.json()['answer']
                st.success(answer)
            else:
                payload=json.dumps(
                {
                "question":question,
                "context":context
                })
                param = "?model="
                model_param= param+model
                final_url = url+model_param
                headers={'Content-Type':'application/json'}
                response = requests.request("POST", final_url, headers=headers, data=payload)
                answer = response.json()['answer']
                st.success(answer)
        else:
            st.error("Question and Context cannot be left empty")
