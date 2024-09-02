'''
Utilizando o type, escreva uma função recursiva que imprima os elementos de uma lista. 
Cada elemento deve ser impresso separadamento, um por linha.
Conside o caso de um lista dentro de listas, como L = [1,[2,3,4,[5,6,7]]].
A cada nível, imprima a lista mais a direita, como fazemos ao identar os blocos em python.
Dica: envie o nível atual como parâmetro e utilize-o para calcular a quantidade de espaços em branco a esquerda de cada elemento.

'''
L = [1,[2,3,4,[5,6,7]]]

def imp_lista(lista):
    for i in lista:
        if type(i) is int:
            print(i)
        else:
            for e in i:
                print(e)
            else:
                for d in e:
                    print(d)

imp_lista(L)