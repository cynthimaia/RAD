from app.model.products import Products
from flask_restful import Resource, reqparse
#reqparse -> utilizada para definir
# e validar os argumentos nas requisoes
#argumentos adicionar
argumentos = reqparse.RequestParser()
#ajuda a validar 
# #os dados recebidos nas requeisoes
argumentos.add_argument('name', type=str)
#deve ser uma string
argumentos.add_argument("price", type=float)
#deve ser um decimal
#argumentos de atualizar
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument("name", type = str)
argumentos_update.add_argument("price", type= float)
argumentos_update.add_argument("id", type=int)
#argumentos deletar
argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument("id", type=int)
class Index(Resource):
    def get(self):
        return "Bem vindo a aplicacao flask"
class ProductCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            ##parse_args -> valida os argumentos passados 
            # e armazena em um dict
            Products.cadastrar_produto(self,
                                       datas["name"], 
                                       datas["price"])
        except Exception as e:  
            return "Status 500"  
class ProductUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Products.atualizar_produto(self, datas["id"], 
                                       datas["name"],
                                         datas["price"])
        except:   
            return "500" 
class Productdelete(Resource):
    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            print(datas)
            Products.delete_products(self,datas['id'])
            return {"message": 'Products delete successfully!'}, 200
        except Exception as e:
            return {'status': 500, 'msg': f'{e}'}