'''Exercício 6.19 Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
• os valores comuns às duas listas
• os valores que só existem na primeira
• os valores que existem apenas na segunda
• uma lista com os elementos não repetidos das duas listas.
• a primeira lista sem os elementos repetidos na segunda '''

lista_a = set([1, 2, 3, 4, 5, 6])
lista_b = set([5, 6, 7, 8, 9])
lista_c = set([])
for e in lista_a: # e é referente a lista 1, ou seja, lista_a
    for i in lista_b: # i é referente a lista 2, ou seja, lista_b
        if e == i: # se o elemento da lista 1 e o elemento da lista 2 forem iguais
            lista_c.add(e) # adicionei os elementos repetidos ao conjunto c


print(f'Os valores comuns as duas listas são: {lista_c}') # Lista onde contem os elementos iguais
print(f'Os valores que só existem na primeira lista são: {lista_a - lista_b}') # Valores que só exitem na primeira lista
print(f'Os valores que só existem na segunda lista são: {lista_b - lista_a}') # Valores que só existem na segunda lista
print(f'Uma lista com elementos não repetidos é igual a: {(lista_a | lista_b) - lista_c } ') # união da lista a com b menos a lista c

            
