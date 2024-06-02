import random

valores_a = []
valores_b = []
intersecao = []

for i in range(20):
    valores_a.append(random.randint(0,50))
    valores_b.append(random.randint(0,50))


print(sorted(valores_a))
print(sorted(valores_b))

for elemento in valores_a:
    if elemento in valores_b and elemento not in intersecao:
        intersecao.append(elemento)

intersecao.sort()
print("A interseção das listas:", intersecao)

for elemento in intersecao:   
    print(f"{elemento}: (lista 1 = {valores_a.count(elemento)}), (Lista 2 = {valores_b.count(elemento)})")  