'''
Escreva uma função que receba uma string com as opções válidas a aceitar (cada opção é uma letra). Converta as opções válidas
para letras minúsculas. 
Utilize input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção é válida.
Em caso de opção inválida, a função deve pedir ao usuário que digite novamente outra opção.
'''

def opcoes():
    while True:
        opc = str(input('Insira uma opção: '))
        if opc.isalpha():
            print('Opção válida')
            opc = opc.lower()
            print(f'Opção [{opc}] selecionada com sucesso!')
            break
        else:
            print('Entrada inválida, tente novamente.')
opcoes()

