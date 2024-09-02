'''
>>> ITERADORES - forma de acesso a uma lista ou estrutura de dados, quando percorremos uma lista com for estamos visitando cada elemento,
sem utilizar índices para acessar cada elemento.

>>> Em python temos a função iter(), que cria um iterador. Iterador é um objeto que trabalha retornandp camadas que retornam o próximo
elemento da sequencia até não haver mais elementos a retornar.

L = [1,2,3] 
t = iter(L) itera a lista
next(t) # Passe por cada elemento da listas
next(t)

>>> O que acontece é que o iterator printa o primeiro elemento depois apaga, e assim sucessivamente\z

# yield

# Utilizamos yield quando estamos trabalhando com MUITAS informações (yield torna processos mais eficientes)
Imagina uma lista muito grande, 10gb, ler essa lista de uma vez, o python terá que armazenar 10gb da memória do seu computador.
Isso pode até dar um memory erro

def ler_arquivo(nome_arquivo):
    linhas = []
    for linha in open(nome_arquivo,'r'):  >>> Não é eficiente pois armazena a lista inteira de uma vez
        linhas.append(linha)
    return linhas

def ler_arquivo(nome_arquivo):
    for linha in open(nome_arquivo,'r'):  >>> O yield vai criar para nós um generator
        yield linha
'''

def ler_csv(nome_arquivo):
    for linha in open(nome_arquivo,'r'):  # >>> O yield vai criar para nós um generator
        yield linha


vendas = ler_csv('t.csv')

for venda in vendas:
    print(venda)