'''
Escreva um programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início.
1 ª string: AABBEFAATT
2ª string: BE
'''
string1 = 'AABBEFAATT'
string2 = 'BE'
print(string2 in string1) # a string 2 está contida na string 1?
print(f'A string2 está na posição {string1.find(string2)} na string 1') # ache na string 1 a string 2