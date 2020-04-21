from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    headline = "Hey, dude!!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Byee Baby"
    return render_template("index.html" ,headline = headline)