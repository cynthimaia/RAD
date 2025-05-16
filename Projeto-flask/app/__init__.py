from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy
app = Flask(__name__)
#uri do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///crud.db'
db = SQLALchemy(app)
"""@app.route("/")
def index():
    #return "<h1> Minha aplicacao em Flask </h1>"
    return render_template("index.html")"""
