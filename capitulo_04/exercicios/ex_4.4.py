# pergunte o sal do funcionario e calcule o valor do aumento. 
# salarios acima de 1250 o aumento é 10 % , inferiores o aumento é 15 %

salario = float(input('Insira o valor do salário: '))
aumento_acima = salario + (salario * 10/100)
aumento_abaixo = salario + (salario * 15/100)
if salario > 1250:
    print(f'Novo salário de R$ {aumento_acima}')
if salario <= 1250:
    print(f'Novo salário de R$ {aumento_abaixo}')