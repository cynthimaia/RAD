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
    def delete_products(self, id):
        try:
            db.session.query(Products).filter(Products.id==id).delete()
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)
    def listar_id(self, products_id):
        try:
            products = db.session.query(Products).filter(Products.id == products_id).all()
            products_dict = [{"id":product.id, 
                               "name":product.name, 
                               "price":product.price} 
                              for product in products] 
            return products_dict  
        except Exception as e: 
            print("Erro ao listar produtos", e)  
