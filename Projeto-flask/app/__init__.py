from flask import Flask

app = Flask("Projeto")

@app.route("/")
def index():
    return "<h1> Minha aplicacao em Flask </h1>"