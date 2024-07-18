#decorator
#route is part of the url after the domain name
#domainName/route

from flask import Flask, render_template,jsonify

app = Flask(__name__)  

JOBS = [
    
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Johannesburg, South Africa',
        'salary': 'R 60 000'
    },
      {
        'id': 2,
        'title': 'AI Engineer',
        'location': 'SAN Fransisco, USA',
        'salary': '$160 000'
    },
     {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$100 000'
        
    }
       
]

@app.route("/")  
def hello_world():  
    return render_template('home.html', jobs=JOBS, company_name="SIM")

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":  
    app.run(debug=True)  
