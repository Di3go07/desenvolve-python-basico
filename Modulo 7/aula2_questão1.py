def encrypt(n):
    x = digitos.index(n)
    return x

data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
digitos = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
separacao = data.split("/")

conversão = encrypt(separacao[1])

print(f"Você nasceu em {separacao[0]} de {meses[conversão]} de {separacao[2]}")