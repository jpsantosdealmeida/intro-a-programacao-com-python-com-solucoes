# Execute o Ex 4.4
# Verifique se o resultado foi o mesmo colocando o else
# Sim, foi
salario = float(input('Insira o valor do salário: '))
aumento_acima = salario + (salario * 10/100)
aumento_abaixo = salario + (salario * 15/100)
if salario > 1250:
    print(f'Novo salário de R$ {aumento_acima}')
else:
    print(f'Novo salário de R$ {aumento_abaixo}')