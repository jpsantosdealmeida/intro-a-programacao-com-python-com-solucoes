# Conjuntos ou set
'''
São estruturas que implementam  operações de união, intersecção e diferença. A principal característica de um conjunto
é que NÃO é permitido repetição de um elemento, e os conjuntos não mantem a ordem de seus elementos
'''
'''
a = set()
a.add(1)
a.add(2)
print(a)
a.add(0)
a.add(-2)
'''

# Podemos testar se um elemento faz parte de um conjunto usando o perador in

# print(1 in a)

# c = set()
# c.add(1,2,3) # Não posso passar mais de um elemento com o add

# Podemos utilizar conjuntos para ver a diferença, utilizamos o operador -
d = {0, 1, 2, 3, -1}
e = {2, 3}
print(d-e) # removeu no d o que tinha no e

# Podemos utilizar conjuntos para fazer a união, utilizamos o operador |
f = {6,8}
print(d | f) # Fez a união do d com f