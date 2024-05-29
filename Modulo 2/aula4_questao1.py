#Leitura de dados (entrada)
comprimento = int(input('Comprimento do terreno: '))
largura = int(input('Largura do terreno: '))
preço_m2 = float(input('Preço do metro quadrado: '))

#Operações (processamento)
area = comprimento * largura
preço_total = preço_m2 * area

#Resultado (saída)
print(f"O terreno possui {area:,} m2 e custa R${preço_total:,.2f}")