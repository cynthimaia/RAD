import sqlite3
from modelo import Pessoa, Marca,Veiculo
banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on") 
#ativar verificacao de chaves estrangeiras
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
            #   ADD motor REAL;''')
#query dinamica
"""comando = '''INSERT INTO Pessoa(cpf,nome, nascimento, oculos)
VALUES(?, ?, ?, ?)
'''
pessoa = Pessoa(92345678, "Pedro", "2000-01-30", True)
#criar um objeto, instanciando da classe pessoa
cursor.execute(comando, (pessoa.cpf, pessoa.nome, 
               pessoa.nascimento, pessoa.usa_oculos))
#lista de objetos
pessoas = [Pessoa(1234567, "Joao", "200-01-31", True),
           Pessoa(987654321008, "Maria", "1995-03-10", False)]
comando2 = '''INSERT INTO Pessoa 
(cpf, nome, nascimento, oculos) 
VALUES (?,?,?,?) '''
cursor.executemany(comando2, [(i.cpf, i.nome,
                               i.nascimento,
                               i.usa_oculos) 
                              for i in pessoas])
pessoa = Pessoa(60345676900, "Joao", 
                "200-01-31", True)
comando3 = '''INSERT INTO Pessoa
(cpf, nome, nascimento, oculos) VALUES (
:cpf,:nome,:nascimento,:usa_oculos);'''
cursor.execute(comando3, {"cpf":pessoa.cpf, 
                          "nome": pessoa.nome, 
                          "nascimento": pessoa.nascimento,
                          "usa_oculos": pessoa.usa_oculos})
pessoa = Pessoa(603456676900,"Joao", "2001-01-31", True)
comando4 = '''INSERT INTO Pessoa(cpf,nome,nascimento,oculos) 
VALUES(:cpf, :nome, :nascimento, :usa_oculos)'''
cursor.execute(comando4, vars(pessoa))
comando1 = '''INSERT INTO Marca(nome, sigla)
 VALUES(:nome, :sigla)'''
marca = Marca("Marca A", "MA")
cursor.execute(comando1, vars(marca))
marca.id = cursor.lastrowid
#lastrowid <-armazena o id da 
#linha do ultimo registro inserido no banco
marcaB = Marca("MarcaB", "MB")
cursor.execute(comando1,vars(marcaB))
marcaB.id = cursor.lastrowid
#veiculos"""
comando2 = '''INSERT INTO Veiculo 
(placa, ano, cor, motor, proprietario, marca)
VALUES (:placa, :ano, :cor, :motor, :proprietario,
:marca)''' 
veiculo1 = Veiculo("AABB00434", "2001",  "Prata", 1234567,  1, 1.0,)
cursor.execute(comando2, vars(veiculo1))

"""comando3 = '''UPDATE Pessoa SET oculos
 = :usa_oculos WHERE cpf = :cpf; '''
cursor.execute(comando3, {"usa_oculos":True,
                          "cpf": 98765432100})
comando4 = '''DELETE FROM Veiculo WHERE
 proprietario = :proprietario'''
cursor.execute(comando4, {"proprietario":98765432100 } )"""

banco.commit()
cursor.close()
banco.close()