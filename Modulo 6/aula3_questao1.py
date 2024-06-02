lista = []
repeticoes = int(input('Quantos números serão adicionados na lista 1 (min 4): '))

for i in range(repeticoes):
    valor = int(input('Digite um número: '))
    lista.append(valor)

print(f'A lista original: {lista}')
print(f'Os três primeiros elementos da lista: {lista[ :3]}')
print(f'Os dois últimos elementos da lista: {lista[ : -3: -1]}')
print(f'A lista ao contrário: {lista[ : :-1]}')
print(f'Elementos nos índices ímpar: {lista[1 : : 2]}')
print(f'Elementos nos índices par: {lista[ : : 2]}')