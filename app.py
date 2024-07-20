#decorator
#route is part of the url after the domain name
#domainName/route

from flask import Flask, render_template,jsonify
from database import load_jobs_from_db


app = Flask(__name__)  


    
@app.route("/")  
def hello_world():  
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs,
                           company_name="SIM")

@app.route("/jobs")
def list_jobs():
    job_list = load_jobs_from_db()
    return jsonify(job_list)

if __name__ == "__main__":  
    app.run(debug=True)  


