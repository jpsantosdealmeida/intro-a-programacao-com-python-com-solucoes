# Lista de ordenção Bubble Sort
# Verifique o que acontece se a lista já está ordenada
# L = [7,4,3,12,8]
L = [1,2,3,4,5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x+1]:
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x+=1
    if not trocou: # Como a lista já está ordenada, ela para aqui
        break
    fim -=1
for e in L:
    print(e)