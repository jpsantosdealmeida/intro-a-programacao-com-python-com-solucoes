# Escreva um programa que verifique se é ou não um número primo
# Para a verificação calcule o resto de divisão por 2 e depois por todos os número ímpares até o número lido
# se o resto de uma dessas divisões for igual a 0 o número não é primo
# 0 e 1 não são primos pois e 2 é o único número primo que é par

# LÓGICA

'''
Verifique se o número é menor ou igual a 1: Números menores ou iguais a 1 não são primos.

Verifique se o número é 2: O número 2 é primo.

Verifique se o número é divisível por 2: Se for, não é primo (pois todos os números pares maiores que 2 não são primos).

Verifique se o número é divisível por qualquer número ímpar de 3 até a raiz quadrada do número:

Se encontrar algum divisor, o número não é primo.
Se não encontrar nenhum divisor, o número é primo.
A razão para verificar até a raiz quadrada é que se um número n pode ser dividido por algum número m, então n = m * k e pelo menos um dos fatores m ou k deve ser menor ou igual à raiz quadrada de n.
'''
print('*'*25)
print('Veficador de números primos')
print('*'*25)
n = int(input('Insira um número para verificar se o mesmo é PRIMO: '))

while True:
    if n < 1:
        print(f'{n} não é PRIMO')
        n = int(input('Insira outro número: '))
    elif n % 2 == 0:
        print(f'{n} não é PRIMO')
        n = int(input('Insira outro número: '))
    else:
        print('É PRIMO')
        break
