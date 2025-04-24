import tkinter as tk
from tkinter import ttk
import modelo
class PrincipalBD():
    def __init__(self, win):
       self.objbd = modelo.AppBd()
       self.janela = win

       self.treeProdutos = ttk.Treeview(self.janela,
                                        columns=("Código do produto",
                                           "Nome", 
                                           "Preco"))
       self.treeProdutos.heading("Código do produto", text= "Id: ")
       self.treeProdutos.heading("Nome", text="Nome: ")
       self.treeProdutos.heading("Preco", text="Preco: ")
       self.treeProdutos.pack() 

       self.nome = tk.Label(self.janela, text="Nome: ")
       self.nome.pack()
       self.entrynome = tk.Entry(self.janela)
       self.entrynome.pack()
       self.preco = tk.Label(self.janela,
                             text="Preco")
       self.preco.pack()
       self.entrypreco = tk.Entry(self.janela)
       self.entrypreco.pack()

       self.btncadastrar = tk.Button(self.janela, 
                                     text="Adicionar produtos",
                                     command=self.cadastrarProduto)
       self.btncadastrar.pack()
    def exibirtela(self):
       try:
          products = self.objbd.select_all_products()
          for product in products:
            self.treeProdutos.insert("", tk.END,
                                      values=product)  
       except:
          print("Nao foi possivel exibir os campos.")
    def cadastrarProduto(self):
      try: 
       name = self.entrynome.get()
       price = float(self.entrypreco.get())
       self.objbd.inserirdados(name, price)

       self.entrynome.delete(0, tk.END)
       self.entrypreco.delete(0, tk.END)
       print("Produto cadastrado com sucesso")
      except:
         print("Nao foi possivel fazer o cadastro.")


janela = tk.Tk() #criar a janela principal
product_app = PrincipalBD(janela)
#janela.title("Bem vindo ao sistema de cadastro!!")
janela.geometry("900x700")
janela.mainloop() 
#apresentar janela, ate que o usuario feche