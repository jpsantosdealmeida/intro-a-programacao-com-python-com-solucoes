'''
Reescreva o programa a seguir de forma a utilizar for em vez de while

def soma(L):
    total = 0
    x = 0 
    while x < 5: # Aqui ele define que a lista tem 5 elementos, se a lista ocnter mais de 5 vai dar erro outofrange
            total += L[x]
            X += 1
    return total


    OBS: PODERIA TER USADO A FUNÇÃO PRÓPIA DO PYTHON 'SUM' para soma da Lista ao inves do total = 0
'''

def soma(L):
    total = 0
    for elemento in range (len(L)): 
        total += L[elemento]
    return total

L = [1,2,3,4,5,6,66,323]
print(soma(L))
print(soma([7,9,12,3,100]))

