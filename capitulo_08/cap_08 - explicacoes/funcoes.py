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