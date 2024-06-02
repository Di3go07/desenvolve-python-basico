lista1 = []
repeticoes1 = int(input('Quantos números serão adicionados na lista 1: '))

for i in range(repeticoes1):
    valores1 = int(input('Digite um número: '))
    lista1.append(valores1)

lista2 = []
repeticoes2 = int(input('Quantos números serão adicionados na lista 2: '))

for i in range(repeticoes2):
    valores2 = int(input('Digite um número: '))
    lista2.append(valores2)

lista_total = lista1 + lista2
intercalado = []

n = 0
count = 1
for i in range(len(lista_total)):
    if count <= len(lista1):
        intercalado.append(lista1[n])
    if count <= len(lista2):
        intercalado.append(lista2[n])
    n += 1 
    count += 1

print(intercalado)