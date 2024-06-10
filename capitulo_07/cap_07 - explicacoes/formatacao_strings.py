'''
Para formatação de Strings podemos usar o .format como ja foi mencionado em capítulos anteriores

Podemos substituir os valores usando números entre chaves. Cdanúmero representa a posição do valor a substituir. A posição é dada 
pela sequência em que os parâmetros são listados na chamada de format.

print('{0} {1}'.format('Alô','Mundo')) # retorno alô mundo
print('{1} {1}'.format('Alô','Mundo')) # retorno mundo mundo
'''
'''
Os números entre chaves é uma refêrencia ao parâmetro passado dentro do format, como 0 a primeira palavra (alô) e 1 ( mundo)
e assim por diante, semelhante a uma lista

print('{0} {1} {0}'.format('-','X')) # retorno - X -

>>> Permite a reordenação de mensagens
print('{1} {0}'.format('primeiro','segundo')) # retorna segundo primeiro

>>> Podemos modificar a largura de cada valor após (:)
print('{1:20} {0}'.format('primeiro', 'segundo')) # retorna segundo              primeiro

>>> Podemos especificar se queremos os espaços adicionais a esquerda ou direita utilizando (<) ou (>)
print('{1:<20} {0}'.format('primeiro', 'segundo')) # retorna segundo              primeiro (A esquerda)
print('{1:>20} {0}'.format('primeiro', 'segundo')) # retorna segundo              primeiro (A direita)

>>> Podmeos centralizar com o (^)
print('{1:^20} {0}'.format('primeiro', 'segundo')) # retorna       segundo        primeiro(centralizado)

>>> Se quisermos outro carctere no lugar do espaço, é so especificar após os (:)
print('{1:-^20} {0}'.format('primeiro', 'segundo')) # retorna ------segundo------- primeiro(centralizado)


>>> Funciona com LISTAS
valores = ['123','456']
             0  ,  1 >>> Indicies
print('{0[1]} {0[1]}'.format(valores))
>>> 0 refere-se ao primeiro (e único) argumento passado para format(), que é a lista ["123", "456"].
>>> [0] refere-se ao primeiro elemento dessa lista, que é "123".

>>> funciona com DICIONÁRIOS
print('{0[nome]} {0[telefone]}'.format({'nome': 'João', 'telefone': 555}))
'''








