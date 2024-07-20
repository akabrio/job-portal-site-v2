from sqlalchemy import create_engine  ,text
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
load_dotenv(".env")  
  
# Connection information  
#server_name = os.environment["server_name"] 
server_name = os.getenv("server_name")  
username = os.getenv("dbuser")  
password = os.getenv("password")   
database_name = os.getenv("database_name")   

# URL encode the password  
encoded_password = quote_plus(password)  
  
# Create the database URL  
database_url = f"mysql+pymysql://{username}:{encoded_password}@{server_name}/{database_name}"  
  
# Create the SQLAlchemy engine  
engine = create_engine(database_url)  
  
  
def load_jobs_from_db():
     with engine.connect() as conn:  
        result = conn.execute(text("SELECT * FROM jobcareers.JOBS")) 
        jobs =[]
        for row in result.all():
            jobs.append(dict(row))
        return jobs