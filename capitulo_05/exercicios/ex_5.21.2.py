# Reescreva o programa anterior porem que continue executando até que o valor digitado seja 0

valor = int(input('Digite o valor a pagar: ')) # valor 250 de exemplo
cedulas = 0
atual = 0
apagar = valor # apagar é igual a 250

while valor != 0: # enquanto apagar for diferente de 0
    atual = 50 # atual recebe 50
    valor = int(input('Digite o valor a pagar: '))
    while True:
        if atual <= valor: # Se 50 for menor ou igual a 250
            valor -= atual # remove 50 do 250                  # Esse bloco diz enquanto isso tudo for verdade continue executando
            cedulas += 1 # a cedulas ganha 1
            
        else:
            if cedulas > 0:
                print(f'{cedulas} cédula(s) de R$ {atual}')
            if apagar == 0:
                break
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0
            
    