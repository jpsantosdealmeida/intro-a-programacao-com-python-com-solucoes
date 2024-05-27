'''
A função for no python é especialmente projetada para percorrer listas.

lista = ['A','B','C']
for elemento in lista:
    print(elemento)
isto é , para cada elemento na lista , printa cada 1
vai retornar A
             B
             C

Vale lembrar que utilizamos for quandos quisermos processar os elementos de uma lista, um a um. Ou quando sabemos a parada
Quando por exemplo um usuário digita varios valeres e 'S' para sair, não daria para utilzar o for pois não sabemos quantos
valores ele vai inserir

Ex. while True:
    n = input('Insira um valor: ')  # no caso serio o while mesmo

Podemos utilizar a função range para gerar listas simples
'''
for v in range(10):  # o 10 não é incluso, vai de 0 a 9
    print(v)
print()
for e in range(5, 10):  # de 5 a 9
    print(e)
print()
for i in range(0, 10, 2):  # vai de 0 a 9, de 2 em 2
    print(i)

L = [22, 34, 55]
for x, e in enumerate(L): # Função enumarate, enumera os elementos dentro da lista
    print(f'{[x]} {e}')
