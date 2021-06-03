import requests
import json
import streamlit as st
import time
import datetime
import os
import pandas as pd

def write(state):
    model = st.text_input('Enter Model Name')
    start_dt = st.date_input('Enter Start Date')
    start_ts = st.time_input('Enter Start Time')
    end_dt = st.date_input('Enter End Date')
    end_ts = st.time_input('Enter End Time')
    start_date = start_dt.strftime("%Y-%m-%d")
    start_time = start_ts.strftime("%H:%M:%S")
    end_date = end_dt.strftime("%Y-%m-%d")
    end_time = end_ts.strftime("%H:%M:%S")
    start_timestamp = start_date+" "+start_time
    end_timestamp = end_date+" "+end_time
    start_unix_ts = str(round(time.mktime(time.strptime(start_timestamp,"%Y-%m-%d %H:%M:%S"))))
    end_unix_ts = str(round(time.mktime(time.strptime(end_timestamp,"%Y-%m-%d %H:%M:%S"))))
    print("Start: ", start_unix_ts)
    print("End: ", end_unix_ts)
    
    url = format(os.environ.get('API_URL'))
    url = url+'answer'
    
    if st.button('Retrieve Question and Answers'):
        if (model == ""):
            url_search = url+"?start="+start_unix_ts+"&end="+end_unix_ts
            print(url_search)
            headers={}
            payload={}
            response = requests.request("GET", url_search, headers=headers, data=payload)
            data = json.loads(response.text)
            output_pd = pd.DataFrame(data)
            st.table(output_pd)
        else:
            url_search = url+"?model="+model+"&start="+start_unix_ts+"&end="+end_unix_ts
            print(url_search)
            headers={}
            payload={}
            response = requests.request("GET", url_search, headers=headers, data=payload)
            data = json.loads(response.text)
            output_pd = pd.DataFrame(data)
            st.table(output_pd)
