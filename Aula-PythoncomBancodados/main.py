import sqlite3
from modelo import Pessoa, Marca,Veiculo
banco = sqlite3.connect('database.db')
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(cpf INTEGER PRIMARY KEY,
               nome TEXT NOT NULL,
               nascimento DATE NOT NULL,
               oculos BOOLEAN NOT NULL);
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
               id INTEGER NOT NULL,
               nome TEXT NOT NULL,
               sigla CHARACTER(2) NOT NULL,
               PRIMARY KEY(id)
               );''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
               placa CHARACTER(7) NOT NULL,
               ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
               proprietario INTEGER NOT NULL,
               marca INTEGER NOT NULL,
               PRIMARY KEY(placa),
               FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
               );''')
#cursor.execute(''' ALTER TABLE Veiculo 
#               ADD motor REAL;''')
#query dinamica
comando = '''INSERT INTO Pessoa(cpf,nome, nascimento, oculos)
VALUES(?, ?, ?, ?)
'''
pessoa = Pessoa(92345678, "Pedro", "2000-01-30", True)
#criar um objeto, instanciando da classe pessoa
cursor.execute(comando, (pessoa.cpf, pessoa.nome, 
               pessoa.nascimento, pessoa.usa_oculos))
banco.commit()
cursor.close()
banco.close()