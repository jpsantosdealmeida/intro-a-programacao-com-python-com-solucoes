# Escreva um programa que converta uma temperatura digitada em C° em F°. A fórmula para essa conversão é F = 9 x C°/5 + 32

temp = float(input('Insira a temperatura em (C°): '))
f =(9 * temp) / 5 + 32

print(f'{temp} C° em F° é {f}')