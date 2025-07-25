from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

connection_string = os.getenv("SQL_CONNECTION_STRING")
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
