print ("responda genero com 'm' ou 'f'")
genero = input("Seu genero: ")
idade = int(input("Sua idade: "))
tempo_trabalho = int(input("Seus anos de trabalho: "))

a = (genero == 'f' and idade >= 60) or (genero == 'm' and idade >= 65)
b = tempo_trabalho >= 30
c = idade >= 60 and tempo_trabalho >= 25
aposentar = a or b or c

if aposentar == True:
    print("Você pode aposentar!")
else:
    print("Ainda falta um tempo...")