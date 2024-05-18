# Escreva um programa que exiba uma lista de opções
# adição,subtração,divisão,multiplicação e sair. Imprima a tabuada da operação escolhida
# Repita até que a opção saída seja escolhida

print('*' * 20)
print('[1] - Adição\n[2] - Subtração\n[3] - Divisão\n[4] - Multiplicação\n[5] - Sair')
print('*' * 20)

opc = int(input('Escolha uma das opções: '))

while not opc == 5:
    if opc == 1:
        n1 = int(input('Insira o primeiro valor para a soma:  '))
        n2 = int(input('Insira o segundo valor para a soma: '))
        print(f'A soma de {n1} e {n2} é {n1+n2}')
        opc = int(input('Escolha uma das opções: '))

    elif opc == 2:
        n1 = int(input('Insira o primeiro valor para a subtração:  '))
        n2 = int(input('Insira o segundo valor para a subração: '))
        print(f'A subtração de {n1} e {n2} é {n1-n2}')
        opc = int(input('Escolha uma das opções: '))
    elif opc == 3:
        n1 = int(input('Insira o primeiro valor para a divisão: '))
        n2 = int(input('Insira o segundo valor para a divisão: '))
        print(f'A divisão de {n1} por {n2} é {n1/n2}')
        opc = int(input('Escolha uma das opções: '))
    elif opc == 4:
        n1 = int(input('Insira o primeiro valor para a multiplicação: '))
        n2 = int(input('Insira o segundo valor para a multipliacação: '))
        print(f'A multiplicação de {n1} por {n2} é {n1*n2}')
        opc = int(input('Escolha uma das opções: '))
    else:
        print('Opção inváida')
        opc = int(input('Escolha uma das opções: '))

print('Programa encerrado, obrigado!')