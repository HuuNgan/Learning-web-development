#using html files

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# How does it find index.html?
# - Flask is only going  to look immediately inside
# of a subdirectory call templates
# - So we have to have in the same folder as application2.py
# a directory call templates, inside of which is index.html
