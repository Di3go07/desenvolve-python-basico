import random

def encrypt (x, key, minchr = 33, maxchr = 127):
    nc = ord(x) + key
    return chr(nc) if nc < maxchr else chr(minchr + (nc % maxchr))

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cripto = []
key = random.randint(1,10)

for i in nomes:
    nome_cripto = list(map(encrypt, i, [key]*len(i)))
    nome_final = "".join(nome_cripto)
    nomes_cripto.append(nome_final)

print(nomes_cripto)