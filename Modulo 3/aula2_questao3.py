print('SE INSCREVA PARA CLUBE JUVENIL DE JOGOS DE TABULEIRO')

nome = input("Diga seu nome: ")
idade = int(input("Diga sua idade: "))
print('Já jogou mais de 3 jogos?(True/False)')
jogos = bool(input('Digite sua resposta: '))
vitorias = int(input("Diga seu número de vitorias em jogo: "))

if idade >= 16 and idade <=18 and jogos >= 3 and vitorias >= 1:
    print(f'{nome} pode ingressar no clube!')
else:
    print(f'{nome} não possui os requisitos necessários!')
