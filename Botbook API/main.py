from typing import Union
from fastapi import FastAPI

import mysql.connector
from mysql.connector import errorcode

import os
import datetime

config = {
  'user': 'root',
  'password': os.environ['MySql'],
  'host': 'localhost',
  'port': '3306',
  'database': 'botbook',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

# Set up connection to MySQL database
# Returns open SQL connection
def OpenMySQLConnection(connection):
    try:
        connection.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
    else:
        print(err)
    
    return connection

# Initialize API application
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/Posts")
def read_posts():
    return {"Test", "Hello"}
