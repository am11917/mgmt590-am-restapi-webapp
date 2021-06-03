import requests
import json
import streamlit as st

def write(state):
    model = st.text_input('Model')
    question =st.text_input('Question')
    context =st.text_input('Context')
    
    url = "https://mgmt590-am-rest-api-wbv4eowlaa-uc.a.run.app/answer"

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
