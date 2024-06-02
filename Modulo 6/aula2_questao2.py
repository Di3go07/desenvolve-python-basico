import random

num_elementos = random.randint(5,20)
valores = []


for i in range(num_elementos):
    valores.append(random.randint(1,10))

soma = sum(valores)
media = sum(valores)/len(valores)

print(f'A lista é {valores}')
print(f'A soma dos valores da lista é {sum(valores)}')
print(f"A média dos valores da lista é {media:.2f}")