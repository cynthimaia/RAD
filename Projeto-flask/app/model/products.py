from app import db
class Products(db.Model):
    __tablename__ = 'Produto'
    __table_args__ = {'sqlite_autoincrement':True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)

    def __init__(self,name, price):
        self.name = name
        self.price = price

    def cadastrar_produto(self, name, price):
        try:
            add_banco = Products(name, price)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as erro:  
            print("Erro ao cadastrar o produto", erro)  

    def atualizar_produto(self,id, name, price ):
        try:
            db.session.query(Products).filter(Products.id == id).update({"name":name, "price":price})
            db.session.commit()
        except Exception as e:  
            print("Erro ao atualizar o produto", e)
    def deletar_produto(self,id):
        try:
            db.session.query(Products)
            .filter(Products.id == id).delete()
            db.session.commit()
        except Exception as e:
            print("Erro ao deletar produto",e)
