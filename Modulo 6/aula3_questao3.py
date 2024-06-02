import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

inicio_intervalo = 0
tamanho_intervalo = 0
max_inicio_intervalo = 0
max_tamanho_intervalo = 0

for i, num in enumerate(lista):
    if num < 0:
        if tamanho_intervalo == 0:
            inicio_intervalo = i
        tamanho_intervalo += 1
    else:
        if tamanho_intervalo > max_tamanho_intervalo:
            max_inicio_intervalo = inicio_intervalo
            max_tamanho_intervalo = tamanho_intervalo
        tamanho_intervalo = 0

del lista[max_inicio_intervalo:max_inicio_intervalo + max_tamanho_intervalo]

print("Editada:", lista)