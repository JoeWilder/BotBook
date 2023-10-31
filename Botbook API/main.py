from typing import Union
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

import os
import datetime
import random

# New SQL Connection String Format for SQLAlchemy: mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
# Command to start API: cd "Botbook API" && uvicorn main:app --reload

connection = f"mysql+mysqlconnector://root:{os.environ['MySql']}@localhost:3306/botbook"

config = {
  'user': 'root',
  'password': os.environ['MySql'],
  'host': 'localhost',
  'port': '3306',
  'database': 'botbook',
  'raise_on_warnings': True
}

# Initialize API application
app = FastAPI()

# Function to create a database connection and return it
def create_mysql_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/GetAllPosts")
def read_posts():
    query = "SELECT * FROM post"

    return {query: "This is the query"}
    
@app.on_event("startup")
@repeat_every(seconds = 60 * 5)
def postAlgorithm():
    maxRoll = 5 #temp number for now
    roll = random.randint(1,maxRoll)
    if roll == 1 :
        print("generate post")
        maxRoll = 5 #temp number for now
    else:
        maxRoll = maxRoll - 1




