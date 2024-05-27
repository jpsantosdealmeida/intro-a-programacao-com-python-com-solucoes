'''
Modifique o programa abaixo de forma a imprimir o menor elemento da lista

L = [1,7,2,4]
maximo = L[0]
for e in L:
    if e > maximo:
        maximo = e
    print(maximo)
'''
L = [1,7,2,4]
minimo = L[-1]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)
