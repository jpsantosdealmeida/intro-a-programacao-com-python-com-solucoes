# Escreva um programa que leia 3 numeros e que imprima o maior e o menor

a = int(input('Número 1 :'))
b = int(input('Número 2 :'))
c = int(input('Número 3 :'))

if a > b and a > c: # A é o maior
    if b > c:
        print('O primeiro valor é maior, o terceiro é o menor') # C é o menor
    if c > b:
        print('O primeiro valor é maior, o segundo é o menor') # B é o menor

if b > a and b > c: # B é o maior
    if a > c:
        print('O segundo valor é maior, e o terceiro é o menor') # C é o menor
    if c > a:
        print('O segundo valor é maior, e o primeiro é o menor') # A é o menor
if c > a and c > b :  # C é o maior
    if a > b:
        print('O terceiro valor é maior, e o segundo é o menor') # B é o menor
    if b > a:
        print('O terceiro valor é maior, e o primeiro é o menor') # A é o menor
