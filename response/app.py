from flask import Flask

app = Flask(__name__)


@app.route("/")
def bit():
    return "0"


@app.route("/<string:name>")
def giveoff(name):
    return f"Hell {name} moth"
