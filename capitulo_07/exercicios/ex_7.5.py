'''
Escreva um programa que leia duas strings e gere uma terceira, na
qual os caracteres da segunda foram retirados da primeira
1 string = AATTGGAA
2 string = TG
3 string = AAAA
'''
'''
Ler as duas strings.
Iterar sobre a primeira string.
Adicionar à terceira string apenas os caracteres que não estão presentes na segunda string.

'''
string_1 = 'AATTGGAA'
string_2 = 'TG'
string_3 = []

for letra in string_1:
    if letra not in string_2:
        string_3.append(letra)
string_3 = ''.join(string_3)
print(f"1 string = {string_1}")
print(f"2 string = {string_2}")
print(f"3 string = {string_3}")