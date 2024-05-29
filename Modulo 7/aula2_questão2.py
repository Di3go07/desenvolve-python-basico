frase = input("Digite uma frase: ")
nova_frase = []
separado = frase.lower().split(" ")

vogais = ["a", "e", "i", "o", "u"]

for i in separado:
    n = 0
    for letra in range (5):    
        substituição = i.replace(vogais[n], "*")
        i = substituição
        n += 1
    nova_frase.append(substituição)

print(" ".join(nova_frase))
