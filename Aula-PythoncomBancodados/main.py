import sqlite3
banco = sqlite3.connect('database.db')
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(
)''')