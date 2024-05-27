# Tamanho de listas

# podemos usar a função len com listas. O valor retorna é igual ao número de elementos presente na lista

# l = [1,2,3]
# print(len(l)) # retorna 3, quantidade de elementos na lista l

# A função len pode ser utilizada em repetições para controlar o limite dos índices
'''
a = [1,2,3]
x = 0
while x < len(a): # Isto é, enquanto x for menor que o tamanho da lsita que é 3, printa e soma mais 1 no x
    print(a[x])
    x += 1 '''

# ADIÇÃO DE ELEMENTOS EM UMA LISTA, UTILIZA-SE O MÉTODO APPEND, FALAREMOS MAIS SOBRE ORIENTAÇÃO A OBJETO NO CAPÍTULO 10

L = [] # L é igual a uma lista vazia
L.append(1) # adicionei um elemento na lista L. OBS: O append joga o elemento no FINAL da lista
print(L)

# Podemos adicionar elementos na lista utilizando +

A = []
A = A + ['A']
A += [2]
print(A)

# ADICIONANDO MAIS DE 1 ELEMENTO A LISTA

lista = [1,5]
lista += [3,4,5] # podemos fazer assim
print(lista)
# ou utilizar outro método, o extends
lista.extend([6,7,8])
print(lista)

# REMOÇÃO DE ELEMENTOS NA LISTA
# para remover utilizamos o del, ele remove e reajusta a lista, seus índices etc

N = ['A','B','C']
del N[0] # delete o elemento no índice 0, no caso o A
print(N)

# para remover o elemento e retornar o mesmo, utiliza-se o pop
N.pop(0)
print(N) # Retornou C, pois o B passou para a primeira posição quando foi feito o Del, e agora removi o 0, o B é o elemento de índice 0

# USO DE LISTAS COMO PILHAS
'''
Em um pilha novos elementos são colocado ao Topo e a retirada também é feita pelo topo.

'''

# Enumarate
'''
lugares_vagos = [10,2,1,3,0] # cada indice representa uma sala, começamos com 1 então é [1,2,3,4,5]
while True:
    sala = int(input('Sala (0 sai): '))
    if sala == 0:
        print('fim')
        break
    if sala > len(lugares_vagos) or sala < 1:
        print('Sala inválida')
    elif lugares_vagos[sala-1] == 0:
        print('Desculpe,sala lotada')
    else:
        lugares = int(input(f'Quantos lugares você deseja ({lugares_vagos[sala-1]} vagos): '))
    if lugares > lugares_vagos:
        print('Esse número de lugares não está disponível')
    elif lugares < 0:
        print('Número inválido')
    else:
        lugares_vagos[sala-1] -= lugares
        print(f'{lugares} lugares vendidos')
print('Utilização das salas')
for x,l in enumerate(lugares_vagos):
    print(f'Sala {x-1} - {l} lugar(es) vazio(s)')
'''

# IMPRIMINDO CADA LETRA DE UMA STRING DENTRO DE UMA LISTA

'''
l = ['maça','banana']
print(l[0][0]) O primeiro 0 representa o índice do elemento, no caso é 0 , e o outro 0 representa a prosição da letra, no caso a primeira é 0
print(l[0][1])
print(l[0][2])
print(l[0][3])
'''

'''

lista = ['pa','ca','da']

for palavra in lista: Para cada palavra na lista e
    for letra in palavra: Para cada letra na palavra
        print(letra)
'''