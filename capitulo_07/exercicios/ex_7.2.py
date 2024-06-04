'''
Escreva um programa que leia duas strings e gere uma terceira com
os caracteres comuns às duas strings lidas.
1 ª string: AAACTBF
2ª string: CBT 

'''
string_1 = 'AAACTBF'
string_2 = 'CBT'
string_3 = ''

for e in string_1: # Para cada elemento na string 1
    for el in string_2: # Para cada elemento na string 2
        if e == el: # Se o elemento da str 1 for igual ao elemento da str 2
            string_3 += e # A string vazia recebe esses elementos
print(f'Os caracteres comuns as 2 listas são: {string_3}')
