from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    k = datetime.datetime.now()
    return render_template("index.html", date=k.date(), time=k.time())
