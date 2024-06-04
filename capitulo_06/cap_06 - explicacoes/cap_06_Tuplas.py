'''
**TUPLAS**

Tupla é uma lista em python, porem, ela é uma lista imutável, isto é, o valor não pode ser alterado
ideal para valores constantes, empacotamento e desempacotamento de valores

Para criarmos uma tupla, ao invés de colchetes [], utilizamos parênteses ()

Ex. 
tupla = ('a','b','c')
print(tupla)
('a','b','c') # retorno do print

PODERIAMOS DECLARAR UMA TUPLA SEM O PARÊNTESES, MAS O PARÊNTESES FACILITA A VISUALIZAÇÃO
Ex.
tupla = 'a','b','c'
print(tupla)
('a','b','c') # retorno do print

tupla[0]
>> 'a'

tupla[1]
>> b

tupla[1:]
>> ('b','c')

tupla * 2
>> ('a','b','c','a','b','c')

len(tupla)
>> 3

Ao tentarmos modificar uma tupla , encontraremos o seguinte erro:
tupla[0] = 'A'
TypeError: 'tuple' object does not support item assignment

utilizando o FOR

for elemento in tupla:
    print(elemento)
>> a
>> b
>> c

## EMPACOTAMENTO ##

tupla = 100,200,300
tupla
>> (100,200,300)

100,200,300 foram convertidos em um tupla com 3 elementos. Essa operação é chamada de empacotamento

## DESEMPACOTAMENTO ##

a,b,c = 10,20,30
a
>> 10
c
>> 30

O primeiro valor (10) foi atribuido a primeira variável (a), e assim sucessivamente...

Podemos também trocar rapidamento os valores de variáveis com construções do tipo:

a,b = 10,20 # a recebe 10 | b recebe 20
a,b = b, a # a recebe b = 20 | b recebe a = 10
a
>> 20
b
>> 10

no caso é interessante pois não utilizamos variáveis temporárias para troca


'''