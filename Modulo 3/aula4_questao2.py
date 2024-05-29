nome = (input('Nome do filme: '))
avaliação = float(input("Estrelas (1 a 5): "))

if avaliação == 1:
    print(f'{nome} avaliado como ruim')
if avaliação > 1 and avaliação <= 2:
    print(f'{nome} avaliado como regular')
if avaliação > 2 and avaliação <= 3:
    print(f'{nome} avaliado como bom!')
if avaliação > 3 and avaliação <= 4:
    print(f'{nome} avaliado como muito bom!')
if avaliação > 4 and avaliação <= 5:
    print(f'{nome} avaliado como excelente')
if avaliação > 5 or avaliação < 1:
    print('avaliação invalida')
