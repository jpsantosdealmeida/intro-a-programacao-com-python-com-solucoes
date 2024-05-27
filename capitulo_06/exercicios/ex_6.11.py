# Modifique o programa abaixo utilizando for e explique porque nem todos os while podem ser transformado em for.
'''
L = []
while True:
    n = int(input('Digite um número (0 sai):' ))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x+=1
'''
L = []
while True: # Esse for não pode ser trocado pois não sabemos quantos números o usuário vai inserir na lista
    n = int(input('Digite um número (0 sai): ' ))
    if n == 0:
        break
    L.append(n)
x = 0
for e in L: # Adicionei um for (para cada e(e = elemento) na lista L)
    print(e) # printa cada 1
    