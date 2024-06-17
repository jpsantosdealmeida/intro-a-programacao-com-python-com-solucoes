'''
Escreva um função que receba 2 números e retorne True se o primeiro for múltiplo do segundo
Valores esperados:
multiplo(8,4) = True
multiplo(7,3) = True
multiplo(5,5) = True

'''

def multiplo(a,b):
    x = a / b
    if x * b == a:
        return True
    else:
        return False
    
print(multiplo(7,3))