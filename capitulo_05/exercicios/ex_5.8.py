# Escreva um programa que leia 2 números, imprima o resultado da multiplicação do primeiro pelo segundo
# Utilize somente soma e subtração
'''
num_1 = int(input('Insira o valor do 1° número: ')) # 4 x 5 = 4 x 4 x 4 x 4 x 4
num_2 = int(input('Insira o valor do 2° número: '))
resultado = num_1 * num_2
x = 0
while x != resultado:
    print(f'{num_1} +',end=' ')
    x += num_1
print(f'= {x}')
    '''
num_1 = int(input('Insira o valor do 1° número: '))
num_2 = int(input('Insira o valor do 2° número: '))
resultado = num_1 * num_2
x = 0
while x != resultado - num_1:
    print(f'{num_1} +', end=' ')
    x += num_1
print(f'{num_1} = {resultado}')


