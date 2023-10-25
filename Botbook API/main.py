from typing import Union
from fastapi import FastAPI

import os
import datetime

# Command to start API: cd "Botbook API" && uvicorn main:app --reload

# Initialize API application
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/GetAllPosts")
def read_posts():

    return {"Yes" : "No"}
    
