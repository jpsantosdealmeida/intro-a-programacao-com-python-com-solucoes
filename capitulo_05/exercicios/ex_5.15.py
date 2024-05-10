# Escreva um programa para controlar um pequena máquina registradora **
# entradas são código do produto {1,2,3,5,9} e a quantidade comprada **
# saída são o total de compras depois que o usuário digitar 0
# Qualquer outra código deve gerar uma mensagem de erro "Código inválido"

total_compra = 0
while True:
    cod_produto = int(input('Insira o código do produto: '))
    if cod_produto == 0:
        break
    quant_comprada = int(input('Insira a quantidade comprada: '))
    if cod_produto == 1:
        total_compra = quant_comprada * 0.50 # 5
    elif cod_produto == 2:
        total_compra += quant_comprada * 1.00 # 10
    elif cod_produto == 3:
         total_compra += quant_comprada * 4.00 # 8
    elif cod_produto == 5:
         total_compra += quant_comprada * 7.00 # 14
    elif cod_produto == 9:
         total_compra += quant_comprada * 8.00 # 16
    else:
        print('Código inválido! ')

print(f'O total da compra foi de R$ {total_compra:5.2f}')