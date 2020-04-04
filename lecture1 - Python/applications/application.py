# route 0
from flask import Flask

app = Flask(__name__)
# __name__ is just representing this current file,
# that this file is going to represent my web application.

# flask is designed in terms of routes, where a route is just part of
# the URL you type in order to determine which page you want to request.
@app.route("/")
def index():
    return "Hello, World!"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/maria")
def maria():
    return "Hello, Maria!"


# TO RUN IT:
# **** On UBUNTU ***
# first: $ export FLASK_APP=application.py
# then:  $ flask run
#-----------------------------------------
# *** On Windows ***
# first: $ set FLASK_APP=application.py
# then:  $ flask run
#-----------------------------------------
# *** On PowerShell ***
# first: $ env:FLASK_APP=application.py
# then:  $ flask run
