# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00

sal = float(input('Insira o salário: '))
if sal > 1200:
    print('Paga imposto')
else:
    print('Não paga imposto')