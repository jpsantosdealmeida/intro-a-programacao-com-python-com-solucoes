'''
>>> FUNÇÃO Random não recebe parametros e retorna valores entre 0 e 1.
import random
for x in range(10):
    print(random.random())

>>> FUNÇÃO uniform retorna valores fracionários dentro de uma determinada faixa
import random
for x in range(10):
    print(random.uniform(15,20))

>>> FUNÇÃO sample escolhe aleatoriamente de uma lista a quantidade de amostras
import random
print(random.sample(range(10,20),6)) # EM OUTRAS PALAVRAS , ENTRE 10 E 20, ESCOLHE 6 NÚMEROS

>>> FUNÇÃO shuffle embaralha os elementos de uma lista
import random
a = list(range(1,10))
random.shuffle(a)    # EM OUTRAS PALAVRAS, A É = UMA LISTA DE 1 A 10, EMBARALHA ESSA LISTA PARA MIM
print(a)

'''