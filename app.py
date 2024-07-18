#decorator
#route is part of the url after the domain name
#domainName/route

from flask import Flask, render_template

app = Flask(__name__)  

@app.route("/")  
def hello_world():  
    return render_template('home.html')

if __name__ == "__main__":  
    app.run(debug=True)  
