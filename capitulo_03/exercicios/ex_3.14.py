# Escreva um programa que pergutne a quant de km percorridos ,quant dias pelo carro foi alugado. 
# Calcule o preço a pagar sabendo que o carra custa R$ 60,00 por dia e R$ 0,15km por km rodado.

quantidade_km = float(input('Quantos Km você rodou? '))
quantidade_dias = int(input('Quantidade de dias alugados: '))

valor_por_km = quantidade_km * 0.15

print(f'O valor total a ser pago é de R$ {valor_por_km + (quantidade_dias*60)}')