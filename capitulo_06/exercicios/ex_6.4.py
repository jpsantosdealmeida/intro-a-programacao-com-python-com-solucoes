# O que acontece quando não verficamos se a lista está vazia antes de chamarmos o método pop?
# Quando a lista estiver vazia irá dar erro no método pop, pois não executará esse método

ultimo = 10
fila = list(range(1, ultimo+1)) # Fila que vai de 1 ao 10


while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print(f'Digite F para adicionar um cliente ao fim da fila,')
    print(f'ou A para realizar o atendimento. S para Sair.')
    operacao = input('Operação(F, A ou S): ')
    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print(f'Fila vazia! Ninguém para atender.')
    elif operacao == 'F':
        ultimo += 1 # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == 'S':
        break
    else:
        print('Operação inválida! Digite apenas F, A ou S!')
            
