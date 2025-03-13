import sqlite3
banco = sqlite3.connect('database.db')
cursor = banco.cursor() #para escrever em sql, inseriri dados, deletar, 
#manipulacoes no banco
#cursor.execute("CREATE TABLE cliente(nome text,idade integer, sexo text)")
cursor.execute("INSERT INTO cliente VALUES ('cynthia', 29, 'f'), ('julio', 30, 'm')")
banco.commit()
cursor.execute("Select * from cliente")
print(cursor.fetchall())
cursor.close()
banco.close()