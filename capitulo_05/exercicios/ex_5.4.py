# Modifique o programa anteriro para imprimir de 1 até o número digitado pelo usuário, somente ímpares
fim = int(input('digite o último número a imprimir: '))
x = 1
while x <= fim:
    if x % 2 == 1:
        print(x)
    x += 1