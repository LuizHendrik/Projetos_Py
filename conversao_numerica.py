import tkinter as tk                  #importando o tkinter para criar a interface gráfica.___________________________________________________________
from tkinter import Label, messagebox #importando as bibliotecas tkinter e messagebox para exibir mensagens.________________________
import numpy as np                    #importando a biblioteca numpy para realizar as operações matemáticas._________________________________


#Propriedades das cores
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

def convert_binario():
     
     #Converte um número decimal para binário._______________________________________________________________________________________________
     
    decimal = int(decimal_entry.get())
    if decimal == 0:
        messagebox.showinfo("Resultado", "0")
    else:
        binario = ''
        while decimal > 1:
            resto = decimal % 2
            decimal = decimal // 2
            binario += str(resto)
        binario += '1'
        messagebox.showinfo("Resultado", f"A conversão do número decimal {decimal} para binário é {binario[::-1]}")

def convert_hexadecimal():
     
     #Converte um número decimal para hexadecimal.___________________________________________________________________________________________
     
    tabela = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
    decimal = int(decimal_entry.get())
    resto = []
    while decimal > 0:
        resto.append(tabela[(decimal % 16)])
        decimal = decimal // 16
    resto.reverse()
    messagebox.showinfo("Resultado", f"A conversão do número decimal {decimal} para hexadecimal é {''.join(resto)}")

def convert_octal():
     
     #Converte um número decimal para octal._________________________________________________________________________________________________
     
    decimal = int(decimal_entry.get())
    if decimal == 0:
        messagebox.showinfo("Resultado", "0")
    else:
        octal = ''
        while decimal > 0:
            resto = decimal % 8
            decimal = decimal // 8
            octal += str(resto)
        messagebox.showinfo("Resultado", f"A conversão do número decimal {decimal} para octal é {octal[::-1]}")

def mostrar_informacoes():
     
    # Mostra as informações da equipe._______________________________________________________________________________________________________
    
    info_janela = tk.Toplevel(root)
    info_janela.title("Informações do Aluno")
    info_janela.geometry("400x300")
    info_janela.configure(bg=co1)
    
    # Adicione os rótulos para exibir as informações_________________________________________________________________________________________
    
    # Hendrik, Victor e Alex
    nome = "Hendrik Mariano"
    rgm = "31175163"
    Label(info_janela, text="Nome: " + nome, bg=co1).pack()
    Label(info_janela, text="RGM: " + rgm, bg=co1).pack()
    
    Label(info_janela, text="-------------------------------------------------------", bg="white").pack()
    
    # Alex
    nome2 = "Alex Gobbo"
    rgm2 = "31433375"
    Label(info_janela, text="Nome: " + nome2, bg=co1).pack()
    Label(info_janela, text="RGM: " + rgm2, bg=co1).pack()
    
    Label(info_janela, text="-------------------------------------------------------", bg="white").pack()
    
    # Victor
    nome3 = "Victor Araujo"
    rgm3 = "32186673"
    Label(info_janela, text="Nome: " + nome3, bg=co1).pack()
    Label(info_janela, text="RGM: " + rgm3, bg=co1).pack()
    
#Inicia a janela principal___________________________________________________________________________________________________________________

root = tk.Tk()
root.title('CONVERSOR DE BASES NUMERICAS')
root.geometry('400x350')
root.configure(bg=co18)

 #Informa o numero Decimal___________________________________________________________________________________________________________________
 
decimal_label = tk.Label(root, text="INFORME O NUMERO DECIMAL:", bg=co5, width=400, height=2, font=('Arial, 13'))
decimal_label.pack()

 #Campo de Entrada do Numero Decimal_________________________________________________________________________________________________________
 
decimal_entry = tk.Entry(root , width=400, font=('Arial, 13'))
decimal_entry.pack()

 #Botoes de Conversão________________________________________________________________________________________________________________________
 
convert_binario_button = tk.Button(root, text="Converter para Binário", command=convert_binario, bg=co5, fg=co1, font=('Arial, 13'))
convert_binario_button.pack(fill=tk.BOTH, expand=True)

convert_hexadecimal_button = tk.Button(root, text="Converter para Hexadecimal", command=convert_hexadecimal, bg=co5, fg=co1, font=('Arial, 13'))
convert_hexadecimal_button.pack(fill=tk.BOTH, expand=True)

convert_octal_button = tk.Button(root, text="Converter para Octal", command=convert_octal, bg=co5, fg=co1, font=('Arial, 13'))
convert_octal_button.pack(fill=tk.BOTH, expand=True)

 #Botao para mostrar as informações dos integrantes__________________________________________________________________________________________
 
details_button = tk.Button(root, text=" Informações", command=mostrar_informacoes, bg=co5, fg=co1, font=('Arial, 13'))#
details_button.pack(fill=tk.BOTH, expand=True)

 #Botao para sair____________________________________________________________________________________________________________________________
 
close_button = tk.Button(root, text="Sair", command=root.quit, bg=co5, fg=co1, border=1)# botao sair com a cor de fundo e cor da fonte
close_button.pack()

 #Iniciando o loop da janela_________________________________________________________________________________________________________________
 
root.mainloop()
