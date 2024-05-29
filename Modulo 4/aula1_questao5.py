N = int(input('Quantas pessoas foram entrevistadas? '))
count = 0 
idades = 0 

while count < N:
    idade = int(input('Idade do entrevistado: '))
    idades += idade
    count += 1

media = idades/N

print(media)