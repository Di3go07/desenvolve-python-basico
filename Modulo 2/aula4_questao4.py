#Leitura de dados (entrada)
valor = int(input('Valor: '))
####as notas só podem ser 1,2,5,10,20,50,100

#Operações (processamento)
centenas = valor // 100
resto = valor % 100
#print(f"sera necessario {centenas} notas de 100")
#print(f"ainda resta {resto} a serem pagos")

valor = resto
cinquenta = valor // 50
resto = valor % 50
#print(f"sera necessario {cinquenta} notas de 50")
#print(f"ainda resta {resto} a serem pagos")

valor = resto
vinte = valor//20
resto = valor%20
#print(f"sera necessario {vinte} notas de 20")
#print(f"ainda resta {resto} a serem pagos")


valor = resto
dez = valor//10
resto = valor%10
#print(f"sera necessario {dez} notas de 10")
#print(f"ainda resta {resto} a serem pagos")

valor = resto
cinco = valor//5
resto = valor%5
#print(f"sera necessario {cinco} notas de 5")
#print(f"ainda resta {resto} a serem pagos")

valor = resto
dois = valor//2
resto = valor%2
#print(f"sera necessario {dois} notas de 2")
#print(f"ainda resta {resto} a serem pagos")

valor = resto
um = valor//1
resto = valor%1
#print(f"sera necessario {um} notas de 1")
#print(f"ainda resta {resto} a serem pagos")


#Resultado (saída)

print("Será necessario: ")
print (f" {centenas} notas de 100,00")
print (f" {cinquenta} notas de 50,00")
print (f" {vinte} notas de 20,00")
print (f" {dez} notas de 10,00")
print (f" {cinco} notas de 5,00")
print (f" {dois} notas de 2,00")
print (f" {um} notas de 1,00")    