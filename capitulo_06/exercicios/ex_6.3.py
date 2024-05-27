# Faça um programa que percorra duas listas e gere uma terceira sem elemento repetidos

lista_a = [1, 3, 5, 7]
lista_b = [2, 3, 5, 8]
lista_c = []

# Adiciona elementos únicos de lista_a
for elemento in lista_a:
    if elemento not in lista_c:
        lista_c.append(elemento)

# Adiciona elementos únicos de lista_b
for elemento in lista_b:
    if elemento not in lista_c:
        lista_c.append(elemento)

print(lista_c)


'''
lista_a = [1,3,5,7]
lista_b = [2,3,5,8]
lista_c = []
x = 0
while x < len(lista_a):
    lista_c.append(lista_a[x])
    x+=1    
x = 0
while x < len(lista_b):
    if lista_c[x] != lista_b[x]:
        lista_c.append(lista_b[x])
        x+=1
    else:
        lista_c.remove(lista_b[x])
print(lista_c)'''
        
        

    
