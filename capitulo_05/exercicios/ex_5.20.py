# O que acontece se digirtamos 0.001? Caso não funcione, altere-o de forma a corrigir o problema.
# Execute o programa 5.1 de cédulas
# Modifique o programa para receber moedas de 0.01,0.02,0.05,0.10 e 0.50.

valor = float(input('Digite o valor a pagar: '))  # 245
cedulas = 0
atual = 100
apagar = valor  # 245
moeda = 0
while True:
    if atual <= apagar:
        if atual >= 1:  # se 100 for menor(<=) ou igual a 245. isso é TRUE
            apagar -= atual  # Apagar recebe 245 - 50                                # Esse laço vai se repetir 4 vezes
            cedulas += 1  # Cedulas ganha 1
        else:
            apagar -= atual
            moeda += 1
   
 
    else:
        if cedulas > 0:
            print(f'{cedulas} cédula(s) de R$ {atual}')
        if moeda > 0:
            print(f'{moeda} moeda(s) de R$ {atual:5.4f} centavos')
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
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        elif atual == 0.01:
            atual = 0.001
        cedulas = 0
        moeda = 0