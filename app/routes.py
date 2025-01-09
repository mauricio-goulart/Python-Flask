from app import app
from flask import render_template

@app.route("/")
@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/index")
def index(): 
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

