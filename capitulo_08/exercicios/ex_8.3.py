'''
Escreva um função que receba o lado de um quadrado e retorne sua área (A = lado²)
valores esperados:

area_quadrado(4) == 16
area_quadrado(9) == 81
'''
def area_quadrado(x):
    A = x**2 # Variável A que recebe o parâmetro e eleva a 2
    return A # Retorna o A
print(area_quadrado(9))