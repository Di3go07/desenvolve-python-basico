import os

frase = input('Digite uma frase: ')

arq = open('modulo 7/frase.txt', 'w')

arq.write(frase)

arq.close()

print(f'Frase salva em: {os.path.abspath('frase.txt')}')