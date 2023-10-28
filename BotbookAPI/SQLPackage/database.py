import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:{os.environ['MySql']}localhost:3306/botbook"

# New SQL Connection String Format for SQLAlchemy: mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()