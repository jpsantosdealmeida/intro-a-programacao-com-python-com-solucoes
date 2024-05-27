# WHILE
# while <condição>: repete o bloco enquanto essa condição for verdadeira
#   bloco

x = 1
while x <= 3:  # enquanto x for menor ou igual a 3, printa x que é 1 e soma com ele com ele mesmo 
    print(x)
    x += 1
    
fim = int(input('digite o último número a imprimir: '))
x = 0
while x <= fim:
    if x % 2 == 0: # só cai aqui se o resto de divisão for 0
        print(x)
    x += 1