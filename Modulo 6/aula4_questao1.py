cemN = []
quadrados = []
divis7 = []
par_impar = []

for i in range(1,101):
    cemN.append(i)
print(cemN[19 : 50 :2])

for i in cemN:
    i *= i
    quadrados.append(i)
print(quadrados)

for i in cemN:
    if i == 0:
        continue
    if i % 7 == 0:
        divis7.append(i)
print(divis7)

for i in range(0,30,3):
    if i % 2 == 0:
        par_impar.append('par')
    else:
        par_impar.append('ímpar')

print(par_impar)

