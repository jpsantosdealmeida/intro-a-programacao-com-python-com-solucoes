# reescreva o programa anterior para escrever os 10 primeiro multiplos de 3
fim = int(input('digite o último número a imprimir: '))
x = 1
while x <= fim:
    if x % 3 == 0:
        print(x)
    x += 1