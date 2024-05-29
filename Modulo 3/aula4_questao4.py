peso = float(input('Digite o peso da carga (kg): '))
distancia = int(input('Digite a distância da entrega (km): '))

if distancia <= 100:
    frete = 1 * peso
if distancia > 100 and distancia <= 300:
    frete = 1.5 * peso
if distancia > 300:
    frete = 2 * peso
elif peso > 10:
    frete += 10

print(f'O frete do produto será: {frete}')