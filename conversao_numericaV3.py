import tkinter as tk
import numpy as np


def converter_base(base):
    try:
        numero      = int(e_valor.get())
        decimal     = str(numero)[2:]
        binario     = bin(numero)[2:] # [2:] pega todos os caracteres da string a partir do terceiro caractere
        octal       = oct(numero)[2:]
        hexadecimal = hex(numero)[2:]
        np.array([numero, binario, octal, hexadecimal])
        
        # Labels
        
        l_binario.config(text="Resultado binário: " + binario)
        l_octal.config(text="Resultado octal: "     + octal)
        l_decimal.config(text="Resultado decimal: " + str(numero))
        l_hexadecimal.config(text="Resultado hexadecimal: " + hexadecimal.upper())
    except ValueError:
        l_binario.config(text="")
        l_octal.config(text="")
        l_decimal.config(text="")
        l_hexadecimal.config(text="")

# Janela

janela = tk.Tk()
janela.title("Conversor de Bases Numéricas")

# Labels e Entrada

label_decimal = tk.Label(janela, text="Número decimal:")
label_decimal.pack()

e_valor = tk.Entry(janela)
e_valor.pack()

# Botões



button_binario = tk.Button(janela, text="Converter para binário", command=lambda: converter_base(2))
button_binario.pack()

button_octal = tk.Button(janela, text="Converter para octal", command=lambda: converter_base(8))
button_octal.pack()

button_hexadecimal = tk.Button(janela, text="Converter para hexadecimal", command=lambda: converter_base(16))
button_hexadecimal.pack()

# Labels de saída
l_binario = tk.Label(janela)
l_binario.pack()

l_octal = tk.Label(janela)
l_octal.pack()

l_decimal = tk.Label(janela)
l_decimal.pack()

l_hexadecimal = tk.Label(janela)
l_hexadecimal.pack()

janela.mainloop()
