
from cProfile import label
from cgitb import text
import os
from tkinter import *
from tkinter import ttk

c=os.path.dirname(__file__)
nomeArquivos = c+"\\cadastro.txt"

def pegarDados():
    file = open(nomeArquivos,'a')
    file.write("Nome do album:.............%s\n" % NomeAlbum.get())
    file.write("Nome do Artista:.............%s \n" % NomeArtista.get())
    file.write("Data Album:.............%s \n" % dataalbum.get())
    file.write("ultimo album: %s \n" % cb.get())

    
    file.write("\n\n")
    file.close()

dados = []
def pegar_nome():
    
    file = open(nomeArquivos,'r')
    for linha in file:
        dados.append(linha)
        print(linha)
    for valor in dados:
        Label(interface,text=valor)
    
    lb['text'] = valor[0]
    lb1['text'] = NomeArtista.get()
    lb2['text'] = dataalbum.get()
    lb3['text'] = cb.get()
    
interface = Tk()

interface.title("Interface")
interface.geometry("500x600")
interface.configure(background='pink')

label1 = Label(interface,text="Nome do Album:",background="pink",foreground="#a736a8")
label1.pack(anchor=W)
NomeAlbum=Entry(interface)
NomeAlbum.pack(anchor=W)



Label(interface,text="Nome Artista:",background="pink",foreground="#a736a8").pack(anchor=W)
NomeArtista=Entry(interface)
NomeArtista.pack(anchor=W)

Label(interface,text="Data album:",background="pink",foreground="#a736a8").pack(anchor=W)
dataalbum=Entry(interface)
dataalbum.pack(anchor=W)

Label(interface,text="ultimo album do artista::",background="pink",foreground="#a736a8").pack(anchor=W)
data=("SIM", "NÃO")
cb=ttk.Combobox(interface, values=data)
cb.pack(anchor=W)


botao = Button(interface,text="Enviar", command=pegarDados)
botao.pack(anchor=W)


botao1 = Button(interface,text="Imprimir", command=pegar_nome)
botao1.pack(anchor=W)

lb = Label(interface, text="")
lb.pack()


lb1 = Label(interface, text="")
lb1.pack()
lb2 = Label(interface, text="")
lb2.pack()

lb3 = Label(interface, text="")
lb3.pack()
interface.mainloop()