nome1 = input("Nome da pessoa: ")
idade1 = int(input("Idade dessa pessoa: "))
nome2 = input("Nome da pessoa: ")
idade2 = int(input("Idade dessa pessoa: "))

if idade1 > 17 or idade2 > 17:
    print(f'{nome1} e {nome2} podem entrar no bar')
else: 
    print(f'{nome1} e {nome2} não podem entrar no bar')