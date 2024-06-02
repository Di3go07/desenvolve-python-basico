URls = ['www.google.com&quot', 'www.gmail.com&quot', 'www.github.com&quot', 'www.reddit.com&quot', 'www.yahoo.com&quot', 'www.google.com&quot']
dominios = []


for i in URls:
    dominio = i[4:-9]
    dominios.append(dominio)

print(dominios)