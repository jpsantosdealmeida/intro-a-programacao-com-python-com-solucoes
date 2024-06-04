# Strings

'''
Podemos acessar strings como listas, mas também strings são imutáveis.
'''
S = 'Alô mundo' # str recebendo alo mundo
# S[0] = 'a' # estou tentando mudar a primeira letra
# print(S) # estou printando a variável
'''
   S[0] = 'a'
    ~^^^
TypeError: 'str' object does not support item assignment

O seguinte erro é apresentando

se quisermos trabalhar caractere a caractere com uma string, alterando o valor, temos que transformá-la em uma lista
'''

L = list(S)
print(L)
# Agora sim poderia modificar os elementos
# A função list transforma cada caractere da string em um elemento da lista, já o método join, faz a operação inversa, transformando os elementos da lista em string

# Verificação parcial de strings

'''
Quando você precisa verificar se uma string começa ou termina com algum caractere, pode usar os métodos startswith e endswith. Eles retornam True or False
'''
print(S.startswith('Al')) # Verificando o início
print(S.endswith('e')) # Verificando o final

# Lembrando que esses métodos verificam exatamente como está a string, isso inclui letra maiusculas e acentuações, podemos usar outro método como o lower ou upper ou captalize para padronizar a string.

frase = 'O Rato Roeu a Roupa do Rei de RomA'
print(frase.upper())
print(frase.startswith('O'))

'''
Outra forma de verificar se uma palavra pertence a uma string é utilizando o in
'''

print(f'Rato 'in frase)

# COUNT
t = 'um tigre, dois tigres, três tigres'
# contando ocorrências de uma letra ou palavra
print(t.count('tigres')) # retorna 2


# PESQUISA EM STRINGS

# Utiliza-se o método find

u = 'Olá Mundo'
#u= '012345678'
print(u.find('M')) # Está na posição 4

'''
Caso a string seja encontrada, o resultado é maior ou igual a 0, ou -1 caso contrário.
'''

'''
Se o objetivo for pesquisar, mas da direita para a esquerda, utilize o método
rflnd, que realiza essa tarefa:
»> s = "Um dia de sol"
>>> s.rfind("d")
7
>>> s.flnd("d")
3
Tanto find quanto rfind suportam duas opções adicionais: início (start) e fim
(end). Se você especificar início, a pesquisa começará a partir dessa posição. Se
especificar o fim, a pesquisa utilizará essa posição como último caractere a coniderar na pesquisa. Por exemplo:
>>> s = "um  tigre, dois tigres, três tigres"
>>> s.find("tigres")
15
>>> s.rfind("tigres")
28
»> s.flnd("tlgres", 7) # iniclo=7
15
>>> s.find("tigres", 30) # iniclo=30
-1
»> s. flnd("tlgres", 0, 10) # lniclo=0 fll'l=10 
'''
