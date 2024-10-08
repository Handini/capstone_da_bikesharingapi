# Capstone API


In most cases when we are running a business, there are a lot of data stakeholder outside our company. The problem is that we need to provide the access in a way that they will not break our security rules or concerns. One way to solve that is by creating an API for the database. In this project, we will introduce you on how python is used for data transaction management using Flask API.

## Project Requirements

**Relevant Topics**:
- Python for Data Analysts (P4DA)
- Exploratory Data Analysis (EDA)
- SQL Query (SQL)

**New Exploratory Topics**:
- Basic Python
    - For loop
    - Custom function
- Build REST API using `flask`

**Workflow**:
- Virtual Environment Preparation
- Read Data from Database
- Create Rest API using Flask API
    - Create Static Analytic Endpoint
    - Create Dynamic Analytic Endpoint
    - Create POST Endpoint
        - Insert Data from CSV to Database
        - Analytic POST Endpoint


## **Usecase**: Bikeshare App

Have you ever rent a bike for faster mobility in town? In the past few years, this business once become a phenomenom. In Indonesia, there are lots of similar services, for example, the Jakarta government's "GOWES" bike sharing service that launcehd in July 2020. 

For the user perspective, the general journey is denoted as follows:
- User scan the bike located at some bike station, sending the data to database as the intent of "start riding"
- Once user has reached its destination station, he/she put back the bike, sending the data again to the database as the intent of "finished riding"

For each activity, there are data transactions between user and database. And how do you think each user's phone communicate with the server for storing and receiving the data? Using API ofcourse! 

We will later create a simplified version of the API service which handles data transactions and analysis. 


**Goals**: Make an API service to connect 3rd party user with data using HTTP request

**End Product**: A Flask API which capable of doing: 
- Input new data to database
- Read specific data from database
- Get specific insight from data analysis process (ie: best performing stations)

**Scoring Metrics**: 

1. 1 point - Created Flask App

-  create app.py file to make flask app
-  create Flask app to execute all of the endpoint you have made

2. 2 points - Created functionality to read or get specific data from the database

- create query to read data from database
- create function to execute read specific information into table from database

3. 4 points - Created functionality to input new data into each table for the databases

- create query to insert new data into stations and trips table
- create function to execute input data into stations and trips table

4. 3 points - Created static endpoints which return analytical result (must be different from point 2,3)

- create query to make analytical resultfrom the data
- create static endpoint to analyze the data from database, for example average trip durations
    
5. 3 points - Created dynamic endpoints which return analytical result (must be different from point 2,3,4)

- create query to make analytical resultfrom the data
- create dinamic endpoint to analyze the data from database, for example average trip durations for each bike_id

6. 3 points - Created POST endpoint which receive input data, then utilize it to get analytical result (must be different from point 2,3,4,5)

- create input data for refering into query for post endpoint
- make query and aggregation function to implement the input

**Tools**: 
- **Python** with **Jupyter Notebook**, installed with **required libraries**
- **Visual Studio Code (VSCode)**: Recommended for writing application scripts
- **TablePlus**: Recommended for easy database access and exploration
- Postman: Optional for easy API testing
