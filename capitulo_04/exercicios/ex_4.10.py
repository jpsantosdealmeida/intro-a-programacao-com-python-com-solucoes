# Escreva um programa que calculo o preço a pagar pelo forncecimento de enercia
# pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencias, I para industrias e C para comercios

quant_energia = float(input('Insira a quantidade de energia em (kWh)'))
opcoes ='''
[1] - Residencial
[2] - Comercial
[3] - Industrial

'''
tipo_instalacao = int(input('Insira sua opção: '))

if tipo_instalacao == 1:
    if quant_energia <= 500:
        print(f'Valor a pagar de R$ {quant_energia*0.40:5.2f}')
    else:
        print(f'Valor a pagar de R$ {quant_energia*0.65:5.2f}')
elif tipo_instalacao == 2:
    if quant_energia <= 1000:
        print(f'Valor a pagar de R$ {quant_energia*0.55:5.2f}')
    else:
        print(f'Valor a pagar de R$ {quant_energia*0.60:5.2f}')
elif tipo_instalacao == 3:
    if quant_energia <= 5000:
        print(f'Valor a pagar de R$ {quant_energia*0.55:5.2f}')
    else:
        print(f'Valor a pagar de R$ {quant_energia*0.60:5.2f}')
else:
    print('Tem algo errado!')
