# Execute o programa 5.1 de cédulas
# Modifique o programa para receber moedas de 0.01,0.02,0.05,0.10 e 0.50.

'''
valor = int(input('Digite o valor a pagar: ')) # 245
cedulas = 0
atual = 100
apagar = valor  # 245

while True:
    if atual <= apagar:  # se 50 for menor(<=) ou igual a 245. isso é TRUE
        apagar -= atual # Apagar recebe 245 - 50                                # Esse laço vai se repetir 4 vezes
        cedulas += 1 # Cedulas ganha 1
    else:
        if cedulas > 0:
            print(f'{cedulas} cédula(s) de R$ {atual}')
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0'''

valor = float(input('Digite o valor a pagar: '))  # 245
moeda = 0
atual = 0.50
apagar = valor  # 245

while True:
    if atual <= apagar:  # se 50 for menor(<=) ou igual a 245. isso é TRUE
        apagar -= atual  # Apagar recebe 245 - 50                                # Esse laço vai se repetir 4 vezes
        moeda += 1  # moeda ganha 1
    else:
        if moeda > 0:
            print(f'{moeda} moeda(s) de R$ {atual}')
        if apagar == 0:
            break
        if atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10

        moeda = 0