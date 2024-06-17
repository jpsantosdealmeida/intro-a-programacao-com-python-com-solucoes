'''
Escreva um função que retorna o maior de dois números.
valores esperados:
maximo(5,6) == True
maximo(7,3) == False
maximo(5,5) == True

avaliando seria
função (parametro 1, parametro 2)
    retorna se o parametro 2 é maior que o parametro 1

'''
def maximo(a,b):
    return True if b >= a else False # Utizei ternário , coloquei tudo em uma linha por ser tratar de um função simples
print(maximo(5,5))