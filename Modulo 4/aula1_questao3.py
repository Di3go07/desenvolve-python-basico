n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

med = (n1+n2+n3)/3

if med>=60:
    print('Aprovado')
elif med>=40 and med <60:
    print('Recuperação')
else:
    print('Reprovado')

print('Fim')
