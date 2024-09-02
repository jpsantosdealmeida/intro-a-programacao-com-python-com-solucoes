'''
Já sabemos como utilizar algumas funções em python, print() é uma função, input,float etc...
Mas agora podemos criar nossas próprias funções

Para definir uma função utilizaremos o def. Veja como declacar uma função de soma que recebe dois números como parâmetros e os imprime na tela

def soma(a,b)
    print(a + b)
'''


def soma(a, b):  # 2 parametros serão passado ao chamar a função
    print(a + b)  # O que faremos com os parâmetros? Um print com a soma


# chamamos a função soma() passamos os parâmetros e executando nos retorna 60
soma(10, 50)


def epar(x): # Definimos uma função epar
    return x % 2 == 0 # ela retorna True se o resto da divisão for 0 e False ser for 1


def impar_par(x): # Outra função impar_par
    if epar(x): # Usamos a função já criada, lemos assim, se for par ou seja, se retornar True, retorne 'Par
        return 'Par'
    else:
        return 'Ímpar' # Se não retorna 'Ímpar'
print(impar_par(3))

"""
>>> UMA FUNÇÃO DEVE RESOLVER APENAS UM PROBLEMA
>>> ISSO A LONGO PRAZO É UMA BOA PRÁTICA PARA EXPORTAR EM OUTRO PROGRAMA
"""
'''
As variáveis globais são aquelas declaradas fora de funções, e podem ser acessada de qualquer parte do código

>>> x = 1
>>> y = 2

Ambas são variáveis globais

def soma():
    total = 0 
>>> A variável total é local, existe somente dentro da função

FUNÇÕES RECURSIVAS

Uma função pode chamar a si mesma, e quando isso acontece chamamos de função recursiva.
Um exemplo seria a função de cálculo de fatorial

função recursiva do fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

>>> PARÂMETROS OPCIONAIS

Nem sempre precisamos passar todos os parâmetros para uma função. preferindo deixar um valor previamente escolhido mas com a possibilidade de alterar.

def barra():
    print('*' * 40) # o print seria **************************************** - 40 asterísiscos

ao invés disso, podemos usar parâmetros opcionais onde podemos tanto utilizar esses valores pré estabelecidos quanto muda-los.

def barra_2(n=40,caractere='*')
    print(caractere * n) # o print seria **************************************** - 40 asterísiscos

o resultado é o mesmo mas poderiamos mudar quando quiser

EX: 
barra(5) o print seria *****
ou
barra(5,'&') # o print seria &&&&&

podemos utilizar o nome do parâmtro para chamar , logo a ordem se torna irrelevante.

barra(n=30,caractere = '/') ou barra(caractere = '/', n=30) OBS: QUANDO ESPECIFICAMOS UM PARAMETRO SOMOS OBRIGADO A ESPECIFICAR O NOME DE TODOS OS OUTROS.



'''
