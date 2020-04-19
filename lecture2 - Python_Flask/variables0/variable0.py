# variable 0
# display variables with html

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello!"
    return render_template("index1.html", headline = headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index1.html", headline = headline)
