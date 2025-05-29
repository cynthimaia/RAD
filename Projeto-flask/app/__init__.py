from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#uri do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///crud.db'
db = SQLAlchemy(app)
from app.model.products import Products
with app.app_context(): #contexto da aplicacao
    db.create_all()
"""@app.route("/")
def index():
    #return "<h1> Minha aplicacao em Flask </h1>"
    return render_template("index.html")"""
