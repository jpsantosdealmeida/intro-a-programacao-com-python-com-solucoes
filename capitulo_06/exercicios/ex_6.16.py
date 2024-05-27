# Modifique o programa para ordenar a lista em ordem decrescente
# L = [1,2,3,4,5] deve ser como L = [5,4,3,2,1]

L = [1, 2, 3, 4, 5]
# L=[1,2,3,4,5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x+1]:  # Se L[0](1) for menor que L[X+1]L[1](2)
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x += 1
    if not trocou:  # Como a lista já está ordenada, ela para aqui
        break
    fim -= 1
for e in L:
    print(e, end=',')
