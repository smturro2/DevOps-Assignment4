# App Overview
- mysql database to hold the data
- flask api to interact with the data
- Seperate streamlit app as a front end
- Seperate docker compose config to hold:
    - Jenkins
    - Selenium for testing


# Docker tips




# Chat gpt queries

- I have a docker compose file. in it i have a docker image which installs python and sets up my flask app. If I make changes to the code what is the fastest way to update it? Currently I delete all the containers and images in docker desktop and do --build, but this takes so long