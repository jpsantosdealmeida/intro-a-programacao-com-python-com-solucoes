# Escreva um programa que calcule o resto da divisão inteira entre dois números.
# Utilize apenas operação de soma e subtração para calcular o resultado.

n1 = int(input('Insira o primeiro valor: ')) # entrada 10
n2 = int(input('Insira o segundo valor: ')) # entrada 3
div = n1 % n2 # saída 1 pois 3 cabe 3 vezes em 10 e sobra 1 
tot = n2
contador = 0

while n2 <= n1: # Enquando 3 for menor que 10
    resto = n1 - n2
    print(f'{n1} - {n2} = {resto}')
    n1 = resto
    contador+=1
print(f'O resto de divisão é: {resto}')


# teste de 15/3
# teste de 25 / 5
# teste de 12/2