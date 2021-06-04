
# ```mgmt590-am-rest-api-webapp``` 
# Question Answering Web App
The Web app has been designed to answer questions, use different transformers models and list recently answered questions, all these functionalities communicate with the REST API through a user friendly portal that only take inputs from clients/users and runs all the necessary methods in the background away from the eyes of a layman and giving the end user a good experience. Features of the webapp:

- The ability to add/remove models from the list of available models
- The ability to answer a question given a context
- The ability to have the user upload a file with questions and contexts and display the resulting answers in a table

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li> <a href ="#architecture-diagram"> Architecture Diagram </a></li>
    <li><a href="#prerequisites-and-installation">Prerequisites & Installation</a></li>  
    <li> <a href ="#functionality-of-the-web-app"> Functionality of the Web App </a></li>
    <ul> 
      <li> <a href="#home"> Home </a></li>
      <li> <a href="#list-models"> List Models </a></li>
      <li> <a href="#add-or-delete-models"> Add or Delete Models </a></li>
      <li> <a href="#ask-a-question"> Ask a Question </a></li>
      <li> <a href="#list-recently-answered-questions"> List Recently Answered Questions </a></li>
       <li> <a href="#upload-question-file-for-answering"> Upload Question File for Answering </a></li>
    </ul>
    <li><a href=#build-and-deploy-web-app-locally> Build and Deploy Web App Locally </a> </li>
  </ol>
</details>


## Getting Started
The web app has been deployed on cloud and it can be invoked using the URL provided. Through the web application we can list all the models, delete and add new models, get answer to our questions and pass the model name but the most important feature is that we can upload a csv file with question and contexts and all the questions in the file will be answered and displayed on the screen.

_**API URL - (Publically Available on Cloud)**_
 ```
      Base URL: https://mgmt590-am-web-app-wbv4eowlaa-uc.a.run.app
 ```

## Architecture Diagram
![image](https://user-images.githubusercontent.com/69768815/120727045-867f3c00-c4a7-11eb-8feb-d2e7020f76a8.png)


### Prerequisites and Installation
To run this web application, you'll need the following pre-requisites installed on your machine

| Library      | Version | Installation |
| ----------- | ----------- | --------- |
| Python | 3.9.1 or above  | <a href="https://www.python.org/downloads/"> Python </a> |
| Streamlit | 0.82.0 | `pip install streamlit`|
| Docker Engine | NA | <a href="https://docs.docker.com/engine/"> Docker </a>|


## Functionality of the Web App
There are multiple methods/paths available that provide functionalities to list, add or delete transformers models. Request an answer to the questions
using the model and listing recently answered questions.

### Home
![image](https://user-images.githubusercontent.com/69768815/120727649-14a7f200-c4a9-11eb-84d3-96782994df6d.png)

### List Models
![image](https://user-images.githubusercontent.com/69768815/120728102-2b027d80-c4aa-11eb-89e2-7a7c546c6b82.png)

### Add or Delete Models
![image](https://user-images.githubusercontent.com/69768815/120728187-5e450c80-c4aa-11eb-8a39-4e0d8c480171.png)

### Ask a Question
![image](https://user-images.githubusercontent.com/69768815/120728569-40c47280-c4ab-11eb-941d-9682314ad775.png)

### List Recently Answered Questions
![image](https://user-images.githubusercontent.com/69768815/120728636-5cc81400-c4ab-11eb-9ce8-a96e8e40dbb9.png)

### Upload Question File for Answering
![image](https://user-images.githubusercontent.com/69768815/120728681-70737a80-c4ab-11eb-8284-bdca1f255dbe.png)


## Build and Deploy Web App Locally
There are two ways to deploy the Web App on your local machine:
</br>
<b> 1. Deployment with Streamlit: </b>
</br>
</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. To deploy the app on your local machine through Streamlit, we just need to run the python file

``` 
>>> streamlit run webapp.py 
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. This will deploy your webapp on your local machine. Post successful deployment of the code
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.0.244:8501

```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. You can access the web app through chrome, edge or any web browser and start sending requests to the REST API through the portal.

<b> 2. Deployment through Docker: </b>

- To deploy the app on your local machine through docker, we need a docker file ,given we already have the application file created, that would be the recipe for docker to build the application
- In the dockerfile, we will add the required dependency of python:3.7-slim
- Once the dockerfile is created, we'll execute the deployment of the docker container which would be published and deployed
- We'll copy the webapp.py in the app folder and the application would run once the docker image was deployed

*Sample Dockerfile*
````
FROM python:3.7-slim

EXPOSE 8080
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install requests streamlit

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "webapp.py"]
````
*Building the Docker Image in the Active Directory/Folder*
```
sudo docker build -t <image-name> . 
```

*Running the Docker Image - with ports defined for communication between local machine and docker image* 
```
sudo docker run -it -p 8501:8501 <image-name> /app/<aap-name>.py
```
