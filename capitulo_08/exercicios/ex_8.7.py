'''
Defina um função recursiva que calcule o maior divisor comum (M.D.C) entre dois números a e b, em que a > b.

mdc(a,b) = | a
           | mdc(b,a-b [a])   b = 0 , a > b
                        b

                        
'''


def euclidiana(a, b):
    if b == 0:  # Se b for igual a o o mdc é a
        mdc = a
    while b != 0:  # Enquanto b for diferente de 0
        a, b = b, a % b  # variável a, variavel b = var a recebe a b, var b é igual o resto de divisão de a por b
    return a  # retorna a e ele está fora do while


print(euclidiana(48, 18))
