'''
Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
l string: CTA
2 string: ABC

'''
string_1 = 'CTA'
string_2 = 'ABC'

# No caso, o T e o B não repetem

for letra in string_1:
    if letra not in string_2:
        string_3 = letra
for elemento in string_2:
    if elemento not in string_1:
        string_3 += elemento
print(f'Os elementos que aparecem somente 1 vez em cada lista são : {string_3}')