# Modifique o programa para trabalhar com 2 filas. Para facilitar seu trabalho, considere o comando A
# para atendimento da fila 1; e B, para atendimento na fila 2. O mesmo para a chegada de clientes.
# F para a fila 1 e G para a fila 2.

ultimo = 10
fila_A = list(range(1, ultimo+1)) # Fila que vai de 1 ao 10
fila_B = list(range(5, ultimo+1)) # Fila que vai de 1 ao 10


while True:
    print(f'\nExistem {len(fila_A)} clientes na fila 1 e {len(fila_B)} na fila 2\n')


    filas = input('A para fila 1 e B para a fila 2: ')
    if filas == 'A':
        print(f'Fila atual: {fila_A}')
        print(f'Digite F para adicionar um cliente ao fim da fila,')
        print(f'ou A para realizar o atendimento. S para Sair.\n')

    elif filas == 'B':
        print(f'Fila atual: {fila_B}')
        print(f'Digite G para adicionar um cliente ao fim da fila,')
        print(f'ou A para realizar o atendimento. S para Sair.\n')

    operacoes = input('Operação(F, A ou S): ')
    
    if 'S' in operacoes:
        break

    for operacao in operacoes: # PARA CADA OPERAÇÃO IN OPERAÇÕES
        if filas == 'A':
            if operacao == 'A':
                if len(fila_A) > 0:
                    atendido = fila_A.pop(0)
                    print(f'O cliente {atendido} foi atendido.')
                else:
                    print(f'Fila vazia! Ninguém para atender.')
            if operacao == 'F':
                ultimo+=1
                fila_A.append(ultimo)

        if operacao == 'A' and filas == 'B':
            if len(fila_B) > 0:
                atendido = fila_B.pop(0)
                print(f'O cliente {atendido} foi atendido.')
            else:
                print(f'Fila vazia! Ninguém para atender.')
        if operacao == 'G':
            ultimo += 1
            fila_B.append(ultimo)

        elif operacao == 'S':
            break