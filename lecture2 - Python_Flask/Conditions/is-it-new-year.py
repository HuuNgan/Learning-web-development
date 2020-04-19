import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def is_it_new_year():
    now = datetime.datetime.now()
    #new_year = now.month == 1 and now.day == 1
    new_year = now.year == 2020
    return render_template("is-it-new-year.html", new_year = new_year)
