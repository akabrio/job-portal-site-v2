#decorator
#route is part of the url after the domain name
#domainName/route

from flask import Flask  

app = Flask(__name__)  

@app.route("/")  
def hello_world():  
    return "<p>Hello, World!</p>"  

if __name__ == "__main__":  
    app.run(debug=True)  
