from sqlalchemy import create_engine, text
from index_db import user, password, host, database

uri = f"postgresql://{user}:{password}@{host}:5432/{database}"
    
db_engine = create_engine(uri)

def connection_database(engine):   
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("Base conectada")
    except Exception as error: 
        print("Error connecting to the database:", error)
       

connection_database(db_engine)