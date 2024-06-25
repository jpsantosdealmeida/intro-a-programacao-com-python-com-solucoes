'''
Escreva um função que receba 2 números e retorne True se o primeiro for múltiplo do segundo
Valores esperados:
multiplo(8,4) = True
multiplo(7,3) = False
multiplo(5,5) = True

'''

def multiplo(a, b): 
    x = a % b # Variavel que recebe o resto de divisão de a por b
    if x == 0: # Se o resto for 0 então retorna True, ou seja, é múltiplo
        return True
    else:
        return False # Se não retorna Falso


print(multiplo(10, 5))
