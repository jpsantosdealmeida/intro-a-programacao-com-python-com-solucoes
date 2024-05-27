# Apresentação de números
numeros = [0,0,0,0,0]
x = 0

while x < 5:
    numeros[x] = int(input(f'Número {x+1}: '))
    x += 1
while True:
    escolhido = int(input('Que posição você quer imprimir (0 para sair): '))
    if escolhido == 0:
        break
    print(f'Você escolheu o número: {numeros[escolhido-1]}')