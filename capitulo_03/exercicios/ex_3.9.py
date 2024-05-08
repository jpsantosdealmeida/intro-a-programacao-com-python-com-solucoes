# Escreva um programa que leia a quantidade de dias,horas,minutos e segundos do usuário.calcule o total de segundos

dias = int(input('dias: ')) # 1 dia = 86.400 segundos
horas = int(input('horas: ')) # 1 hora = 3600 segundos
min = int(input('minutos: ')) # 1 min = 60 segundos
seg = int(input('segundos: ')) # 1 segundo

print(f'{dias} dias,{horas} horas, {min * 60} minutos e {seg} segundos\nequivale ao total de {(dias * 86400) + (horas * 3600) + (min * 60) + seg} segundos')