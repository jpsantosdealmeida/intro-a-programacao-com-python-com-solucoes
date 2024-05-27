# Altere o programa de forma a poder trabalhar com vários comandos digitados de uma vez só.
# Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string.


ultimo = 10
fila = list(range(1, ultimo+1)) # Fila que vai de 1 ao 10

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print(f'Digite F para adicionar um cliente ao fim da fila,')
    print(f'ou A para realizar o atendimento. S para Sair.')
    
    operacoes = input('Operação(F, A ou S): ')
    if 'S' in operacoes:
        break

    for operacao in operacoes: # PARA CADA OPERAÇÃO IN OPERAÇÕES
        if operacao == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'O cliente {atendido} foi atendido.')
            else:
                print(f'Fila vazia! Ninguém para atender.')
        if operacao == 'F':
            ultimo+=1
            fila.append(ultimo)
        elif operacao == 'S':
            break
        
                
    