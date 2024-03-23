import tkinter
from tkinter import *
from tkinter import ttk
import numpy

#cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca / white
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = '#e89613'  # laranja
co6 = "#8c8c8c"  # cinza
co7 = "#ff0000"  # vermelho
co8 = "#00ff00"  # verde
co9 = "#0000ff"  # azul
co10 = "#ffff00" # amarelo
co11 = "#ff00ff" # magenta
co12 = "#00ffff" # ciano
co13 = "#800000" # marrom
co14 = "#008000" # verde escuro
co15 = "#000080" # azul escuro
co16 = "#808000" # oliva
co17 = "#800080" # roxo
co18 = "#008080" # teal
co19 = "#c0c0c0" # prata

#Mostrar informacoes

def mostrar_informacoes():
    
    # Defina as informações do aluno aqui
    
    #Hendrik
    nome = "Hendrik Mariano"
    rgm = "31175163"
    
    #Alex
    nome2 = "Alex Gobbo"
    rgm2 = "31433375"
    
    #Victor
    nome3 = "Victor Araujo"
    rgm3 = "32186673"
    
    # janela para exibir as informações
    
    info_janela = Toplevel(janela)
    info_janela.title("Informações do Aluno")
    info_janela.geometry("400x300")
    info_janela.configure(bg=co1)
    
    
        
    # Adicione os rótulos para exibir as informações
    
    #Hendrik
    Label(info_janela, text="Nome: "        + nome, bg=co1).pack()
    Label(info_janela, text="RGM: "         + rgm, bg=co1).pack()
       
    Label(info_janela, text="-------------------------------------------------------", bg="white").pack()
    #Alex
    Label(info_janela, text="Nome: "        + nome2, bg=co1).pack()
    Label(info_janela, text="RGM: "         + rgm2, bg=co1).pack()
    
    Label(info_janela, text="-------------------------------------------------------", bg="white").pack()
    #Victor
    Label(info_janela, text="Nome: "        + nome3, bg=co1).pack()
    Label(info_janela, text="RGM: "         + rgm3, bg=co1).pack()

janela = Tk()
janela.title('CONVERSOR')
janela.geometry('400x350')
janela.configure(bg=co18)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1,ipadx=190)

#Janelas de dois frames

frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

#frame cima

app_nome = Label(frame_cima, text="Conversor de base numerica", relief=FLAT, anchor='center', font=('System 20'), bg=co2, fg=co1)
app_nome.place(x=10, y=15)

    #Funcao converter
def converter():
    
    
    def numero_para_decimal(numero, base):
    
    # O número decimal correspondente
        decimal     = int(numero, base)
        binario     = bin(decimal)
        octal       = oct(decimal)
        hexadecimal = hex(decimal)
        

            # Converte (int), (bin), (oct) e (hexa) para string
        
        l_binario['text']     = str(binario[2:])
        l_octal['text']       = str(octal[2:]) 
        l_decimal['text']     = str(decimal) 
        l_hexadecimal['text'] = str(hexadecimal[2:].upper())
        
        
    numero = e_valor.get()
    base = combo.get()
    
    #definindo o valor da base
    if base == 'BINARIO':
        base=2
    elif base == 'OCTAL':
        base=8
    elif base == "DECIMAL":
        base=10
    else:
        base = 16    
        #chamando funcao
    numero_para_decimal(numero, base)
        
    
#frame baixo configurando

bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
combo = ttk.Combobox(frame_baixo,width=12, justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x=20, y=10)


e_valor = Entry(frame_baixo, width=9, justify='center', font=("",13), highlightthickness=1, relief='solid')
e_valor.place(x=175, y=10)

#BOTAO
b_converter = Button(frame_baixo,command=converter, text="CONVERTER", relief=RAISED, overrelief= RIDGE, font=('Ivy 8 bold'), bg=co1, fg=co4)
b_converter.place(x=280, y=10)

b_info = Button(frame_baixo, text="Info", command=mostrar_informacoes, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold'), bg=co1, fg=co4)
b_info.place(x=320, y=60)
l_binario = Label(frame_baixo, text="BINARIO",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co15, fg=co1)
l_binario.place(x=35, y=60)
l_binario = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_binario.place(x=170, y=60)
l_octal = Label(frame_baixo, text="OCTAL",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co12, fg=co1)
l_octal.place(x=35, y=100)
l_octal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_octal.place(x=170, y=100)
l_decimal = Label(frame_baixo, text="DECIMAL",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co13, fg=co1)
l_decimal.place(x=35, y=140)
l_decimal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_decimal.place(x=170, y=140)
l_hexadecimal = Label(frame_baixo, text="HEXADECIMAL    ",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_hexadecimal.place(x=35, y=180)
l_hexadecimal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_hexadecimal.place(x=170, y=180)
janela.mainloop()
