import random

valores = []

for i in range(20):
    valores.append(random.randint(-100,100))


print(valores)
print("A lista organizada:", sorted(valores))
print("O índice do maior valor da lista original:", valores.index(max(valores)))
print("O índice do menor valor da lista original:", valores.index(min(valores)))