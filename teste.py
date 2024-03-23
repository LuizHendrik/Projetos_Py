import tkinter as tk
from tkinter import Label, messagebox

# Definição das cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # Branca
co2 = "#6f9fbd"  # Azul
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = '#e89613'  # Laranja

def convert_binario():
    """Converte um número decimal para binário."""
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
    """Converte um número decimal para hexadecimal."""
    tabela = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
    decimal = int(decimal_entry.get())
    resto = []
    while decimal > 0:
        resto.append(tabela[(decimal % 16)])
        decimal = decimal // 16
    resto.reverse()
    messagebox.showinfo("Resultado", f"A conversão do número decimal {decimal} para hexadecimal é {''.join(resto)}")

def convert_octal():
    """Converte um número decimal para octal."""
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
    """Mostra as informações dos alunos."""
    # Janela para exibir as informações
    info_janela = tk.Toplevel(root)
    info_janela.title("Informações do Aluno")
    info_janela.geometry("400x300")
    info_janela.configure(bg=co1)
    
    # Adiciona os rótulos para exibir as informações dos alunos
    # Hendrik
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

# Inicializando a janela principal
root = tk.Tk()
root.title('CONVERSOR DE BASES NUMÉRICAS')
root.geometry('400x350')
root.configure(bg=co0)

# Rótulo para informar o número decimal
decimal_label = tk.Label(root, text="INFORME O NÚMERO DECIMAL:", bg=co5, font=('Arial', 13))
decimal_label.pack()

# Campo de entrada para o número decimal
decimal_entry = tk.Entry(root, width=30, font=('Arial', 13))
decimal_entry.pack()

# Botões para conversão
convert_binario_button = tk.Button(root, text="Converter para Binário", command=convert_binario, bg=co2, fg=co1, font=('Arial', 13))
convert_binario_button.pack(fill=tk.BOTH, expand=True)

convert_hexadecimal_button = tk.Button(root, text="Converter para Hexadecimal", command=convert_hexadecimal, bg=co2, fg=co1, font=('Arial', 13))
convert_hexadecimal_button.pack(fill=tk.BOTH, expand=True)

convert_octal_button = tk.Button(root, text="Converter para Octal", command=convert_octal, bg=co2, fg=co1, font=('Arial', 13))
convert_octal_button.pack(fill=tk.BOTH, expand=True)

# Botão para mostrar informações dos alunos
details_button = tk.Button(root, text="Informações", command=mostrar_informacoes, bg=co2, fg=co1, font=('Arial', 13))
details_button.pack(fill=tk.BOTH, expand=True)

# Botão para sair do programa
close_button = tk.Button(root, text="Sair", command=root.quit, bg=co2, fg=co1)
close_button.pack()

# Iniciando o loop principal da janela
root.mainloop()
