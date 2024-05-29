print('PREENCHA SUA FICHA DE PERSONAGEM')
print("Escolha entre 'mago', 'guerreiro' e 'arqueiro'")
classe = input('Classe: ')
print("Escolha seu pontos de força (1 a 20)")
forca = int(input('Pontos de força: '))
print("Escolha seu pontos de magia (1 a 20)")
magia = int(input('Pontos de magia: '))

if classe == 'guerreiro' and forca >= 15 and magia <= 10:
    print('Pontos de atributo consistentes com a classe escolhida: True')
elif classe == 'mago' and forca <= 10 and magia >= 15:
    print('Pontos de atributo consistentes com a classe escolhida: True')
elif classe == 'arqueiro' and forca > 5 and magia > 5 and magia < 15 and forca < 15:
    print('Pontos de atributo consistentes com a classe escolhida: True')
else:
    print('Pontos de atributo consistentes com a classe escolhida: False')

 
