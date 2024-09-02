'''
Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada
como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.
'''
def validacao(var,list):
        if var in list:
            return True
        else:
            return False
lista = ['a','b','c']
print(validacao('a',lista))