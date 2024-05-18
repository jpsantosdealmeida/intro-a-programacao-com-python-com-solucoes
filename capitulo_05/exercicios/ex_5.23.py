# Escreva um programa que verifique se é ou não um número primo
# Para a verificação calcule o resto de divisão por 2 e depois por todos os número ímpares até o número lido
# se o resto de uma dessas divisões for igual a 0 o número não é primo
# 0 e 1 não são primos pois e 2 é o único número primo que é par

numero = int(
    input('Insira um número para verificar se é ou não um número primo: '))
primo = numero % 2

for n in range(2, numero):
    primo % n
    if primo == 0:
        print('Não é primo')
   
1