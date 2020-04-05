from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def list_names():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("list_names.html", names = names)
