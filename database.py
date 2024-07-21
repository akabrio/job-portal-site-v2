#Go into database and get the information based on the information provided in the url and returns json

from sqlalchemy import create_engine, text  
from urllib.parse import quote_plus  
from dotenv import load_dotenv  
import os  
  
# Load environment variables from .env file  
load_dotenv(".env")  
  
# Connection information  
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
        jobs = []  
        for row in result.all():  
            jobs.append(dict(row))  
        return jobs  
    
#we get the value of id from the url
def load_job_from_db(ID):
    with engine.connect() as conn:
        result=conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            val=ID
        )
    
        rows = result.all() 
        if len(rows) == 0:
             return None
        else:
            return dict(rows[0])
        

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email,  education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 #linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])