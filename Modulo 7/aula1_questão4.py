numero = (input("Digite seu número de telefone: "))
numero_completo = numero


if len(numero) == 8:
    counter = 1
    numero_quebrado1 = " "
    n = 0
    while counter <= 4:
        numero_quebrado1 += numero[n]
        n += 1
        counter += 1

if len(numero) == 9:
    counter = 1
    numero_quebrado1 = " "
    n = 0
    while counter <= 5:
        numero_quebrado1 += numero[n]
        n += 1
        counter += 1


counter = 1
numero_quebrado2 = " "
n = -4
while counter <= 4:
    numero_quebrado2 += numero[n]
    n += 1
    counter += 1




if len(numero) < 9:
    print(f"Numero completo: 9{numero_quebrado1} -{numero_quebrado2}")

if len(numero) == 9:
    if numero[0] != "9":
        print("Número de telefone não reconhecido!")
    if numero[0] == "9":
        print(f"Numero completo: {numero_quebrado1} -{numero_quebrado2}")


    

