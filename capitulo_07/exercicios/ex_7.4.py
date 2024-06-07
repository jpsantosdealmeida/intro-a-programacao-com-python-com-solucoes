'''
Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC 
resultado
T: 2x
A: 2x
C: 1x

'''

string_1 = 'TTAAC'
contagem = {}
for elemento in string_1:
   if elemento in contagem:
       contagem[elemento] +=1
   else:
       contagem[elemento] = 1
for letra,frequencia in contagem.items():
    print(f'{letra}:{frequencia}x')
   

