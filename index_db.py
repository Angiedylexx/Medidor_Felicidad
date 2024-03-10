import os

from dotenv import load_dotenv

load_dotenv()

user =  os.getenv("DB_USERNAME")
database =  os.getenv("DB_DATABASE")
password =  os.getenv("PASSWORD")
port =  os.getenv("PORT")
host =  os.getenv("DB_HOST")