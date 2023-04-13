from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/hi-poop")
def hi_poop_cookie():
    return render_template("hi_poop.html", title="HI POOP")

@app.route("/about")
def about():
    return render_template("about.html", title="About Poop")