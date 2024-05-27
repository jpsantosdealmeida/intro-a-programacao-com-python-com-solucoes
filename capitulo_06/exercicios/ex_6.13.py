# A lista de temperatura de Mons, na Bélgica, foi armazenada na lista 
# T = [-10,-8,0,1,2,5,-2,-4]
# Faça um programa que imprima a menor e a maior temperatura , assim como a temperatura média

T = [-10,-8,0,1,2,5,-2,-4]
maior = T[0]
menor = T[-1]

for e in T:
    if e > maior:
        maior = e
    elif e < menor:
        menor = e
print(f'A maior temperatura é {maior} é a menor é {menor}')