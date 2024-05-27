# Escreva um programa que verifique se um número é palíndromo.
# Um número é palíndromo e continua o mesmo caso seus dígitos sejam invertidos.
# Ex. 454, 10501

n = str(input('Insira um número para verificar se é palíndromo: '))
# rint(n[::-1])

for numero in range(len(n) -1,-1, -1):
    n1 = n[::-1]
    if n1 == n:
        print('É Palíndromo')
        break
    else:
        print('Não é Palíndromo')
        break