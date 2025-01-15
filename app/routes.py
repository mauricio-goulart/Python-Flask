from app import app
from flask import flash,redirect,request,render_template

@app.route("/", defaults = {"nome":"drake"})
@app.route("/base", defaults = {"nome":"drake"})
@app.route("/base/<nome>")
def base(nome):
    return render_template("base.html", nome = nome)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if (usuario == "admin") and (senha == "debug"):
        return f"usuario: {usuario} e senha: {senha}"
    else:
        flash("Errou, o usuario é admin e a senha é debug" )
        return redirect("/login")

    

@app.route("/index")
def index(): 
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")
 
