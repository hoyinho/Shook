from flask import Flask, render_template,session,redirect
import os
import utils
import betsQuery

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<link>")
def quickLink():
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/bet")
def bet():
    return render_template("bet.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.debug = True
    app.secret_key = "random ke here"
    app.run(host='0.0.0.0', port=8000)
