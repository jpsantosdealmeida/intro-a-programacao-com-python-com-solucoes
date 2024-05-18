# Faça um programa que solicite um preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

preco_mercadoria = float(input('Valor da mercadoria: '))
desconto = int(input('Desconto de: '))
desconto_calculado = preco_mercadoria - (preco_mercadoria * desconto/100)

print(f'Desconto de {desconto} % recebido com sucesso. Preço a pagar de R$ {desconto_calculado:.2f}')