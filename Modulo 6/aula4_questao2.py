frase = (input('Digite uma frase: '))
lista_vogal = []
lista_consoante = []


for i in frase:
    i = i.lower()
    if i == ' ':
        continue
    if i in 'aeiou':
        lista_vogal.append(i)
    else:
        lista_consoante.append(i)


print(sorted(lista_vogal))
print(sorted(lista_consoante))
