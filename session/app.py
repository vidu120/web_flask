from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("note") is None:
        session["note"] = []
    notes = request.form.get("note")
    session["note"].append(notes)
    return render_template("index.html", notes=session["note"])
