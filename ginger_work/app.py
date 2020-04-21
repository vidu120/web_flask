from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    fine = True
    return render_template("index.html", fine=fine)


@app.route("/<int:uptil>")
def find(uptil):
    fine = False
    return render_template("index.html", fine=fine, uptil=uptil)
