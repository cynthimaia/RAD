notas = [("Carlos", 2.0), ("Lucas", 10.0),
          ("Maria", 5.5)]
with open("notas.txt", "w") as arquivo:
    for nome, nota in notas:
        arquivo.write(f"Nome: {nome},Nota: {nota}\n")

try:
    with open("notas.txt", "r") as arquivo:
     arquivo.read()
except FileNotFoundError as e:
   print("Arquivo inexistente", e)
