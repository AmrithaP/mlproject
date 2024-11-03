import os
import sys # custom exceptoion and logging handle required hence
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql

load_dotenv() # loads all env variables

host = os.getenv('host')
user = os.getenv('user')
pwd = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
  logging.info("Reading SQL database started")
  try:
    mydb = pymysql.connect(
      host = host,
      user = user,
      password = pwd,
      db = db
    )
    logging.info("Connection established", mydb)
    print("Connection established")

    df = pd.read_sql_query('Select * from student', mydb)
    print(df.head())
    return df

  except Exception as e:
    raise CustomException(e)


