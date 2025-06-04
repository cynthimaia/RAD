from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
app = Flask(__name__)
#uri do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///crud.db'
api = Api(app)
db = SQLAlchemy(app)
from app.model.products import Products
with app.app_context(): #contexto da aplicacao
    db.create_all()
from app.view.reso_products import Index,ProductCreate, ProductUpdate, Productdelete
api.add_resource(Index, "/")
api.add_resource(ProductCreate,"/inserir")
api.add_resource(ProductUpdate, "/atualizar")
api.add_resource(Productdelete, "/deletar")
"""@app.route("/")
def index():
    #return "<h1> Minha aplicacao em Flask </h1>"
    return render_template("index.html")"""
