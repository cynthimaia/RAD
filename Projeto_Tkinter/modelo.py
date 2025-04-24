import sqlite3
class AppBd():
    def __init__(self):
        self.create_table()
    def abrirconexao(self):
        try:
            self.connect = sqlite3.connect("database.db")
        except sqlite3.Error as erro:
            print("Falha ao se conectar ao banco de dados", erro)
    def create_table(self):
        self.abrirconexao()
        create_table_query = """CREATE TABLE IF NOT EXISTS products(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                price REAL NOT NULL); """
        try:
            cursor = self.connect.cursor()
            cursor.execute(create_table_query)
        except sqlite3.Error as erro:
            print(f"Falha ao criar tabela: {erro}")
        finally: #finalizacao, independente do try e except
            if self.connect:
                cursor.close()
                self.connect.close()
                print("A conexao com o sqlite foi fechada.")
    def inserirdados(self, name, price):
        self.abrirconexao()
        insert_query = """ INSERT INTO products
          (name, price) VALUES (?, ?)"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(insert_query, (name, price))
            print("Produto cadastrado com sucesso!!")
            self.connect.commit()
        except sqlite3.Error as erro:
            print("Falha ao inserir produto")
        finally:
            if self.connect:
                cursor.close()
                self.connect.close()
                print("A conexao com o sqlite foi fechada!!")
    def select_all_products(self):
        self.abrirconexao()
        select_query = """SELECT * FROM products"""
        products = []
        try:
            cursor = self.connect.cursor()
            cursor.execute(select_query)
            products = cursor.fetchall() 
            #recuperar todos os registros
        except  sqlite3.Error as error:
                print("Falha ao retornar produtos", error)
        finally:
            if self.connect:
                cursor.close()
                self.connect.close()
                print("A conexao com o sqlite foi fechada")
        return products
    def update_product(self, id, name, price):
        self.abrirconexao()
        update_query = """UPDATE products SET name = ?, price = ?
        WHERE id = ?"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(update_query, (name, price, id))
            self.connect.commit()
            print("Produto atualizado com sucesso")
        except sqlite3.Error as error:
            print("Falha ao atualizar o produto")
        finally:    
            if self.connect:
                cursor.close()
                self.connect.close()
                print("A conexão com o sqlite foi fechada.")
    def delete_product(self, id):
        self.abrirconexao()
        delete_query = """DELETE FROM products WHERE id=?"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(delete_query, id)
            self.connect.commit()
        except sqlite3.Error as error:
            print("Falha ao deletar o produto")
        finally:    
            if self.connect:
                cursor.close()
                self.connect.close()
                print("A conexão com o sqlite foi fechada.")
        



