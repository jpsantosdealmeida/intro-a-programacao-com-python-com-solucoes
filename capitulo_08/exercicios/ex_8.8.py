'''
Usando a função mdc definida no exercício anterior, defina uma função para calcular o menor múltiplo comum (M.M.C) entre dois números.

mmc(a,b) = | a * b
           | mdc(a,b)


em que a*b pode ser escreotp como abs
'''


def euclidiana(a, b):
    if b == 0:  # Se b for igual a o o mdc é a
        mdc = a
    while b != 0:  # Enquanto b for diferente de 0
        a, b = b, a % b  # variável a, variavel b = var a recebe a b, var b é igual o resto de divisão de a por b
    return a  # retorna a e ele está fora do while


def func_menor(a,b): # declarei outra função para o mmc
    abs = (a*b) # como o exercicos falou a variável abs é igual a multiplicação do parametro a * b
    calculo = abs//euclidiana(a,b) # variavel calculo é igual ao a*b (resto de div inteira) função euclidiana que chamei que calcula o mdc
    return calculo # retorna o valor
print(func_menor(48,12)) # pedi para calcular com o a valendo 48 e o b valendo 12