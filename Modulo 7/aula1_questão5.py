frase = input("Digite uma frase: ")

num_vogais = 0
indices = []

for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        num_vogais += 1
        indices.append(i)

print(f"A frase tem {num_vogais} vogais")
print(f"Indices: {indices}")

