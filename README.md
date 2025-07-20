# App Overview
- mysql database to hold the data
- flask api to interact with the data
- Seperate streamlit app as a front end
- Seperate docker compose config to hold:
    - Jenkins
    - Selenium for testing



# To ask
- network
- .env management
- running containers in jenkins
- cant get condition to work for frontend

# Docker tips




# Chat gpt queries

- I have a docker compose file. in it i have a docker image which installs python and sets up my flask app. If I make changes to the code what is the fastest way to update it? Currently I delete all the containers and images in docker desktop and do --build, but this takes so long
- I'm running jenkins in a docker container. I currently have a webhook setup and it pulls the code and is able to run the ehllo world Jenkinsfile i ahve in my repo. Now how do I get jenkins to run my docker-compose.yml thats in my repo?
- Pytest using selenium. How do I test a click on run and then make sure the data came up