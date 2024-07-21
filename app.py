#decorator
#route is part of the url after the domain name
#domainName/route

from flask import Flask, render_template,jsonify, request
from database import load_jobs_from_db, load_job_from_db,add_application_to_db


app = Flask(__name__)  


    
@app.route("/")  
def hello_world():  
    jobs = load_jobs_from_db()
    #return jsonify(job_list)
    return render_template('home.html', 
                           jobs=jobs)

@app.route("/jobs")
def list_jobs():
    job_list = load_jobs_from_db()
    return jsonify(job_list)
    

#create dynamic route (id will be recieved as a parameter)
@app.route("/job/<ID>")
def show_job(ID):
        job = load_job_from_db(ID)
        #return jsonify(job)
         #render template
        #inside the jobpage template  any reference to job it will get the value from load_job_from_db()
        
        if not job:
            return "Not found", 404
        return render_template('jobpage.html',
                               job=job)
        

      
@app.route("/job/<ID>/apply", methods=['post'])
def apply_to_job(ID):
  data = request.form
  job = load_job_from_db(ID)
  add_application_to_db(ID, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)
# store this in the DB
# send an email
# display an acknowdgement
 
if __name__ == "__main__":  
    app.run(debug=True)  


