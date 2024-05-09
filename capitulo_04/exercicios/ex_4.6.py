# Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km. calcule o preço da passagem cobrrando 0,50
# por km para viagens de até 200 km, e 0,45 para viagens mais longas

distancia = float(input('Insira a distância em km: '))
passagem = 0

if distancia <= 200:
    passagem = passagem + (distancia * 0.50)
    print(f'O valor da passagem é {passagem}')
else:
     passagem = passagem + (distancia * 0.45)
     print(f'O valor da passagem é {passagem}')
