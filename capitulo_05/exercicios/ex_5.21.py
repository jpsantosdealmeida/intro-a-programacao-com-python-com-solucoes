# Reescreva o programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas.

valor = int(input('Digite o valor a pagar: ')) # 245
cedulas = 0
atual = 50
apagar = valor  # 245

while True:
    if atual <= apagar:  # se 50 for menor(<=) ou igual a 245. isso é TRUE
        apagar -= atual # Apagar recebe 245 - 50                                # Esse laço vai se repetir 4 vezes
        cedulas += 1 # Cedulas ganha 1
    else:
        if cedulas > 0:
            print(f'{cedulas} cédula(s) de R$ {atual}')
        if apagar == 0:
            valor = int(input('Digite o valor a pagar: ')) 
            apagar = valor
            if valor == 0:
                break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0