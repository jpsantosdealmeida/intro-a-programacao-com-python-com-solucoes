# Escreva um programa que pergunte a velocidade. caso a velocidade ultrapasse 80km. Exiba um print dizendo que o usuario foi multado.
# Nesse caso exiba o valor da multa cobrando R$ 5,00 por km acima de 80

velocidade = int(input('Qual a sua velocidade: '))

if velocidade <= 80:
    print('Ok...')
if velocidade > 80:
    print(f'Você recebeu a multa e o valor é R$ {(velocidade-80) * 5}')
