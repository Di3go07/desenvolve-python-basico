import random

num = int(random.randint(1,10))

while True:
    chute = int(input('Digite um número: '))
    diferença = abs(chute - num)
    if chute == 0:
        break
    if chute == num:
        print(f'Correto! O número misterioso é {num}')
        break
    if diferença >= 4:
        print('Muito alto! Tente novamente')
    if diferença <= 3:
        print('Muito baixo, tente novamente')
