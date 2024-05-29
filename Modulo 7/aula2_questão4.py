#Pelo menos 8 caracteres de comprimento.
#Contém pelo menos uma letra maiúscula e uma letra minúscula.
#Contém pelo menos um número.
#Contém pelo menos um caractere especial (por exemplo, @, #, $).

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
caracteres_especiais = ["#", "@", "$", "&", "*"]  

def validador_senha(senha):
    condicao1 = False
    condicao2 = False
    condicao3 = False
    condicao4 = False
    condicao5 = False

    x = 0
    for i in range(len(caracteres_especiais)):
        if caracteres_especiais[x] in senha:
            condicao1 = True
        x += 1
    n = 0
    for i in range(len(numeros)):
        if numeros[n] in senha:
            condicao2 = True
        n += 1
    if len(senha) >= 8:
        condicao3 = True
    for i in senha:
        if ord(i) >= 65 and ord(i) <= 90:
            condicao4 = True
    for i in senha:
        if ord(i) >= 91:
            condicao5 = True

    if condicao1 and condicao2 and condicao3 and condicao4 and condicao5 == True:
        return True 
    else: return False

senha1 = "Senha123@"
senha2 = "senhaFraca"
senha3 = "Senha_fraca12" 

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False