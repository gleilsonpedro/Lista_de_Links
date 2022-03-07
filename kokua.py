from ctypes import alignment
from operator import truediv
from turtle import left
import webbrowser
from tkinter import *
from tkinter import messagebox

#funções
def linha():
    lb_espaco = Label(app, text="_______________________________________________", font=("Arial 14"))
    lb_espaco.pack()

def espaco():
    lb_espaco = Label(app, text="", font=("Arial 8"))
    lb_espaco.pack()
def painel():
    new=2
    url="http://10.27.2.122/svo/public/login"
    webbrowser.open(url,new=new)

#janela centralizada na tela
janela=Tk()
janela.title("KOKUA")
janela.iconbitmap("waraba.ico")
# configura janela para abrir centralizada em qualquer tela
largura = 600
altura = 400
#seta a largura e altura da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
# faz o calculo pra centralizar a janela no meio da tela
pos_x = largura_tela/2 - largura/2
pos_y = altura_tela/2 - altura/2
#define as variáveis pra centralizar a tela
janela.geometry("%dx%d+%d+%d" % (largura, altura, pos_x, pos_y))

lb_topo = Label(janela, text="Principais links necessários", font="Arial 14", width=600,
               height=1, bg="gray", fg="white")
lb_topo.pack()

lb_link1 = Label(janela, text="abre o painel pra chamar a senha", font="Arial 12",  bg="white", fg="blue")
lb_link1.pack(side=LEFT)

bt_link1 = Button(janela, text= "Painel de Chamados", comman=painel, 
                 font="Arial 12", bg= "gray",
                 fg="white")
bt_link1.pack(side=LEFT)

texto = Widget





janela.mainloop()

#new=2
#url="http://10.27.2.122/svo/public/login"
#webbrowser.open(url,new=new)



#####Atualizado#####
#import webbrowser
#new=2
#site =str(input('Digite um site: '))
#url="https://www."+site+"/"
#
#webbrowser.open(url,new=new)
