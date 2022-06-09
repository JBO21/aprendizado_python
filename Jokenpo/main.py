import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

# configuração da Janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

#divisão janela
top_tela = Frame(janela, width=260, height=100, bg=co1, relief='raised')
top_tela.grid(row=0, column=0, sticky=NW)
top_bot = Frame(janela, width=260, height=200, bg=co0, relief='flat')
top_bot.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


janela.mainloop()
