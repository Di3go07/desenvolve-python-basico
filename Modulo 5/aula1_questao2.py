import math
import random

x = int(input('Digite a quantidade de repetições: '))
soma = 0 

for i in range(x):
    num = random.randint(0,100)
    soma += num

raiz_quadrada = math.sqrt(soma)

print(f'A raiz quadrada soma dos número é {raiz_quadrada:.2f}')