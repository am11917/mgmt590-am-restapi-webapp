import requests
import json
import streamlit as st
import os
import pandas as pd

def write(state):
    
    answer = []
    questions = []
    contexts = []
    
    url = format(os.environ.get('API_URL'))
    url = url+'models'
    qa_file = st.file_uploader("Upload CSV",type=['csv'])
    headers={}
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    output_pd = pd.DataFrame(data)
    option = st.selectbox("Select Model", options = output_pd['name'])    
    
    if st.button("Process"):
        if qa_file is not None:
            url = format(os.environ.get('API_URL'))
            url = url+'answer'
            model_cmd="?model="+option
            url=url+model_cmd
            file_details = {"Filename":qa_file.name,"FileType":qa_file.type,"FileSize":qa_file.size}
            st.write(file_details)
            df = pd.read_csv(qa_file)
            for idx, row in df.iterrows():
                context = row['context']
                question = row['question']
                contexts.append(context)
                questions.append(question)
                payload=json.dumps(
                {
                "question":question,
                "context":context
                })
                headers={'Content-Type':'application/json'}
                response = requests.request("POST", url, headers=headers, data=payload)
                answer.append(response.json()['answer'])                
                
            output = {'question':questions,'context':contexts,'answer':answer}
            output_pd = pd.DataFrame(output)
            st.table(output_pd)
