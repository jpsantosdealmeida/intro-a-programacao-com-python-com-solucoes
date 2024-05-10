# Escreva um programa que leia números inteiros
# O programa deve ler números até que o usuário digite 0.
# No final imprima a quantidade de números digitadas, a soma e a média.

contador = 0
soma = 0
while True:
    inteiros = int(input('Insira números inteiros: '))
    if inteiros == 0:
        break
    soma += inteiros
    contador += 1
print(f'Você inseriu {contador} números, a soma é {soma} e a média é {soma/contador:5.2f}')
