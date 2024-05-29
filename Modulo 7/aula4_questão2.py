import os

frase = open('modulo 7/frase.txt', 'r')


with open('modulo 7/palavra.txt', 'w') as copia:
    for i in frase:
        linha = i
    n = 0
    linha_corrigida = ""
    for i in linha:
        if ord(linha[n]) >= 65 and ord(linha[n]) <= 90:
            linha_corrigida += linha[n]
        elif ord(linha[n]) >= 91 and ord(linha[n]) <= 122:
            linha_corrigida += linha[n]
        elif ord(linha[n]) >= 126:
            linha_corrigida += linha[n]
        elif linha[n] == " ":
            linha_corrigida += linha[n] 
        n += 1

    print(" ")
    print(f"A mensagem original era: {linha}")
    print("-"*100)

    for i in linha_corrigida:
        palavra = linha_corrigida.split(" ")
    n = 0
    for x in range(len(palavra)):
        palavra_separada = palavra[n] + "\n"
        copia.write(palavra_separada)
        n += 1
    

with open('modulo 7/palavra.txt', 'r') as terminal:
    print("A mensagem editada:", "\n",terminal.read())