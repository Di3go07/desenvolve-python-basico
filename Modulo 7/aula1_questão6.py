frase = input("Digite uma frase: ")
objetivo = input("Digite a palvra objetivo: ")

palavras = frase.lower().split(" ")
print(palavras)

anagramas = []

for i in palavras:
    if sorted(i) == sorted(objetivo): #amor -> amor
        anagramas.append(i)           # roma -> amor

print(anagramas)