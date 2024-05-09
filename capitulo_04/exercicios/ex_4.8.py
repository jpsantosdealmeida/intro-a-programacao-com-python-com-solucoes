num_a = int(input('Insira o primeiro valor: '))
num_b = int(input('Insira o segundo valor: '))

msg = '''
[1] - Soma
[2] - Subtração
[3] - Divisão
[4] - Multiplicação
'''
print(msg)
resposta = int(input('Qual sua opção: '))
if resposta == 1:
    print('Você escolheu soma')
    print(f'{num_a} + {num_b} = {num_a+num_b}')
elif resposta == 2:
    print('Você escolheu subtração')
    print(f'{num_a} - {num_b} = {num_a - num_b}')
elif resposta == 3:
    print('Você escolheu divisão')
    print(f'{num_a} / {num_b} = {num_a/num_b}')
elif resposta == 4:
    print('Você escolheu multiplicação')
    print(f'{num_a} * {num_b} = {num_a * num_b}')
else:
    print('Opção inválida')