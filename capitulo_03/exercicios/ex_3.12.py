# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem

dist = float(input('Distância prevista a percorrer[km]: '))
velocidade_media = int(input('Velocidade média esperada[km/h]: '))
tempo_viagem = dist / velocidade_media

print(f'Tempo previsto de {tempo_viagem} horas')