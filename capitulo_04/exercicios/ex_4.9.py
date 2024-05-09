# Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
# pergunte o valor da casa, salario e quantidade de meses que deseja pagar.
# O valor da parcela é o valor da casa dividido pelo numero de meses
# o valor da parcela não pode ultrapaassar 30% do salário

valor_casa = float(input('Qual o valor da casa que deseja comprar: '))
salario = float(input('Qual o valor do salário: '))
meses = int(input('Deseja pagar em quantos meses: '))
parcela = valor_casa / meses
valor_limite = (salario*(30/100))

if parcela <= valor_limite:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')