# Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal.
# Pergunte o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e total de juros pago.



vl_inicial = float(input('Insira o valor inicial da dívida: R$ '))
vl_pago_mensal = float(input('Valor a pagar da dívida mensalmente: R$ '))
vl_juros = float(input('Insira a taxa de juros mensal da dívida: '))
total_juros_divida = 0
meses_para_pagamento = int(vl_inicial / vl_pago_mensal)
mes = 1

while mes != meses_para_pagamento: 
    juros = (vl_inicial * vl_juros/100)  # Calculo de juros
    vl_inicial += juros
    print(f'{mes}° mes = {juros:5.2f}, valor total da dívida = {vl_inicial:5.2f}')
    meses_para_pagamento = int(vl_inicial / vl_pago_mensal)
    mes += 1
    total_juros_divida += juros
print(f'meses para a quitação = {(meses_para_pagamento)+1} meses, total de juros pago R$ {total_juros_divida:5.2f},total pago R$ {vl_inicial:5.2f} ')
