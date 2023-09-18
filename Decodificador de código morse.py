#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


#esse é o dicionário criado para o mapeamento de letras, números e espaços para o código morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '}  #espaço

#este código apresenta, basicamente, duas funções principais. A primeira é a morse_to_text(morse code) que converte o código morse em texto. A segunda é a text_to_morse(text), que faz o caminho inverso da primeira, ela converte texto em morse.
#função para converter morse em texto
def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')  #separe os caracteres morse por espaço
    decoded_text = []

    for char in morse_code:
        decoded_text.append([k for k, v in morse_dict.items() if v == char][0])

    return ''.join(decoded_text)

#função para converter texto em morse
def text_to_morse(text):
    text = text.upper() #a função upper condiciona a leitura de letras maiúsculas apenas
    morse_code = []

    for char in text:
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else:
            morse_code.append('?') #quando o programa não encontrar o caracter indicado pelo usuário, ele retornará '?'

    return ' '.join(morse_code)
#nessa parte de entrada do usuário, o código permite que ele escolha a conversão que irá fazer. Sendo escolhida, o programa faz a leitura e exibe o resultado na tela.
#o loop principal permite que o usuário faça quantas conversões quiser até sair do programa.
#exemplo para rodar:
choice = input("Escolha a conversão (1 - Morse para Texto, 2 - Texto para Morse): ")

if choice == '1':
    morse_code = input("Digite o código Morse: ")
    decoded_text = morse_to_text(morse_code)
    print("Texto decodificado:", decoded_text)
elif choice == '2':
    text = input("Digite o texto ou números: ")
    morse_code = text_to_morse(text)
    print("Código Morse:", morse_code)
else:
    print("Escolha inválida.")


# In[ ]:





# In[ ]:





# In[ ]:




