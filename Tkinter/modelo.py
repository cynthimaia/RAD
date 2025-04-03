import sqlite3
class AppBd():
    def abrirconexao(self):
        try:
            self.connect = sqlite3.connect("database.db")
        except sqlite3.Error as erro:
            print("Falha ao se conectar ao banco de dados", erro)
    def create_table(self):
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
        insert_query = """ INSERT INTO products
          (name, price) VALUES (?, ?)"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(insert_query, (name, price))
            print("Produto cadastrado com sucesso!!")
        except sqlite3.Error as erro:
            print("Falha ao inserir produto")
        finally:
            if self.connect:
                cursor.close()
                self.connect.close()
                print("A conexao com o sqlite foi fechada!!")

