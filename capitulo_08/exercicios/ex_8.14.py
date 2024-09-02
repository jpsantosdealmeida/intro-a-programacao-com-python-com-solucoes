'''
OBS (NO LIVRO ESTÁ COMO EXERCÍCIO 8.13)
Programa 8.20 - adivinhando o número
import random
n = random.randint(1,10)
x = int(input('Escolha um número entre 1 e 10: '2))
if x == n:
    print('Você acertou!')
else:
    print('Você errou.')
    
REFAÇA ESSE PROGRAMA DE FORMA QUE O USUÁRIO TENHA 3 CHANCES. O PROGRAMA TERMINA SE O USUÁRIO ACERTAR OU ERRAR TRÊS VEZES.
'''
import random
n = random.randint(1,10)
tentativas = 0
while True:
    x = int(input('Escolha um número entre 1 e 10: '))
    if x == n:
        print('Você acertou!')
        break
    else:
        print('Você errou.')
        tentativas += 1
        if tentativas == 3:
            print(f'Você errou {tentativas} vezes')
            break
