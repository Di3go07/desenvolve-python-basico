n = int(input("Total de experminetos: "))
cont = 0 
sapo, coelho, rato = 0, 0, 0

while cont < n:
    tipo = input("Tipo de cobaia: ")
    quantia = int(input("Quantidade da cobaia: "))
    if tipo == "S":
        sapo += quantia
    elif tipo == "R":
        rato += quantia
    elif tipo == "C":
        coelho += quantia
    elif tipo == "parar":
        break
    
    cont +=1
    

total_cobaias = sapo + rato + coelho

print("")
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {coelho/total_cobaias * 100}")
print(f"Percentual de ratos: {rato/total_cobaias * 100}")
print(f"Percentual de sapos: {sapo/total_cobaias * 100}")

