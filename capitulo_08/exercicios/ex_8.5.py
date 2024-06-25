'''
Reescreva a função do programa pesquisa em lista de forma a utilizar os métodos de pesquisa em lista, vista no capítulo 7.
'''


def pesquise(lista, valor):
    Lista = list(lista)  
    for x in range (len(Lista)):
        if lista[x] == valor:
            return x
    return None  

string = 'ola mundo'
print(pesquise(string,'m'))

