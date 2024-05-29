produto1_nome = input('Digite o nome do produto 1: ')
produto1_valor = float(input('Digite o preço unitário do produto 1: '))
produto1_quantidade = float(input('Digite a quantidade do produto 1: '))

produto2_nome = input('Digite o nome do produto 2: ')
produto2_valor = float(input('Digite o preço unitário do produto 2: '))
produto2_quantidade = float(input('Digite a quantidade do produto 2: '))

produto3_nome = input('Digite o nome do produto 3: ')
produto3_valor = float(input('Digite o preço unitário do produto 3: '))
produto3_quantidade = float(input('Digite a quantidade do produto 3: '))

valor_total = (produto1_valor * produto1_quantidade) + (produto2_valor * produto2_quantidade) + (produto3_valor * produto3_quantidade)

print(f'Total da compra: R${valor_total:,.2f}')