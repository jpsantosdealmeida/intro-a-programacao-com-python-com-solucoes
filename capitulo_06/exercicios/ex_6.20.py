'''
 Escreva um programa que compare duas listas. Considere a primeira
lista como a versão inicial e a segunda como a versão após alterações. Utilizando
operações com conjuntos, seu programa deverá imprimir a lista de modificações
entre essas duas versões, listando:
• os elementos que não mudaram
• os novos elementos
• os elementos que foram removidos 
'''
lista_inicial = set([1,2,'a','b','c']) # Lista inicial
lista_final = set([2,'a','b',3]) # Lista após a mudança

print(f'Elementos que não mudaram: {lista_inicial & lista_final}') # Simbolo de intersecção, elementos que não mudaram, estão presente em ambos conjuntos
print(f'Elemento novo: {lista_final - lista_inicial}') # Elemento novo
print(f'Elemento que foram removidos: {lista_inicial - lista_final}')


