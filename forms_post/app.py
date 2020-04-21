from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/name", methods=["POST"])
def person():
    k = request.form.get("name")
    return render_template('name.html' , name = k)
