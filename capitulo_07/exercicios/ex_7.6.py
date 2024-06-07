'''
Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira,
dos caracteres da segunda pelos da terceira
1 stringa = AATTCGAA
2 string = TG
3 string = AC
resultado = AAAACCAA

Criar um dicionário de mapeamento onde cada caractere da segunda string mapeia para o caractere correspondente na terceira string.
Iterar sobre a primeira string, substituindo cada caractere conforme o mapeamento do dicionário.
Construir a string resultante com as substituições realizadas.
Imprimir a string resultante.

'''
string_1 = 'AATTCGAA'
string_2 = 'TG'
string_3 = 'AC'
mapeamento = {}
x = 0


for letra in string_2:
    mapeamento[letra] = string_3[x]
    x += 1
print(mapeamento)

resultado = []
for caractere in string_1:
    if caractere in mapeamento:
        resultado.append(mapeamento[caractere])
        print(resultado)
    else:
        resultado.append(caractere)