# Modifique o programa de forma a pesquisar p e v em toda a lista e informando o usuário
# a posição onde p e a posição onde v foram encontradas.

L = [10,15,20,25,28]
p = int(input('Digite o 1° valor a procurar na lista: '))
v = int(input('Digite o 2° valor a procurar na lista: '))
x = 0
''''''
for elemento in L: # Para cada elemento na lista L
    while x < len(L):
        if L[x] == p:
            print(f'{p} encontrado na posição {x}')
        elif L[x] == v:
            print(f'{v} encontrado na posição {x}')
        x+=1
if p or v not in L[x]:
    print('Elemento não encontrado')