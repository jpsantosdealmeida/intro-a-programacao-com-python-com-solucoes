# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

valor_salario = float(input('Valor do salário para cálculo: '))
aumento = float(input('Porcentagem do aumento: '))

print(f'Seu novo salário é {valor_salario + (valor_salario * aumento / 100)}')