# LISTAS  são um tipo de variável, que permite o armazenamento de vários valores do mesmo tipo, tipos diferentes, outras listas ou uma lista vazia.

# Listas são flexiveis e podem crescer ou diminuir

# O tamanho da lista é igual a quantidade elementos dentro da lista

# O indice da lista é sua posição, inicia no 0, assim, uma lista de tamanho 6 vai de 0 a 5

L = []  # Declaramos com colchetes uma lista
# lista vazia

# agora uma lista z com 3 elementos

z = [15, 8, 9]  # O tamanho da lista é 3, porem para acessar o 15, o indice é 0!!!
#    0, 1 ,2
print(z[0])  # Retornou o elemento no índice 0 que é o 15

# Utilizando o nome da lista e o índice, podenos mudar o conteúdo de um elemento

z[0] = 1
print(z[0])  # mudei o primeiro elemento que era 15 para 1
print(z)  # agora a lista contem os elementos [1,8,9]

# programinha de calculo da media com 5 valores que são ás notas

notas = [6, 7, 5, 8, 9]
soma = 0
x = 0  # x inicia com 0 pois uma lista o primeiro elemento da lista é a posição 0
'''
while x < 5: # enquanto x for menor que 5:
    soma += notas[x] # a variável soma recebe ela mais a lista notas[x] (x vai de 0 a 4) pegando todos os elementos da lista e colocando na variável soma
    print(x)
    x+=1
print(f'Média: {soma/x:5.2f}') # calculo da média'''


# CÓPIA E FATIAMENTO

a = [1, 2, 3]  # uma lista com 3 elementos
b = a  # b é igua a A
print(f'Lista 1 = {a}\nLista 2 = {b}')
b[0] = 5 # aqui eu estou mudando o primeiro elemento da lista b
print(f'Lista 1 = {a}\nLista 2 = {b}')

# mas nota-se que a lista a também mudou, isso aconteceu pois na verdade b é somente um apelido para a lista a
# ou seja, a lista a e b são a mesma lista, se eu modficar em a ou em b , na verdade estou modficando as 2 

# PARA EFETIVAMENTE FAZER UMA COPIA UTILIZAMOS [:]

c = [3,4,5,]
d = c[:] # fiz uma cópia da lista c
d[0] = 10 # mudei o primeiro elemento da lista d para 10
print(d) # imprimindo as 2 listas, somente a d mudou, pois agora sim é uma cópia


# PODEMOS TAMBÉM FATIA A LISTA IGUAL AS STRINGS

e = [10,20,30,40,50]
print(e[:5])
print(e[2:5]) # do 2 elemento que é o 20 até o 5, porem não incui o 2
print(e[1:3]) # não incui o 1 e imprime somente o 2 e o 3
print(e[-1]) # ultimo elemento da lista, e o penultima é -2, e assim sucessivamente