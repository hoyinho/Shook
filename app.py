from flask import Flask, render_template,session,redirect

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.debug = True
    app.secret_key = "random ke here"
    app.run(host='0.0.0.0', port=8000)
