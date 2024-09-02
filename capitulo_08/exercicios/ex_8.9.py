'''
Reescreva a função para cálculo de seqência de Fibonacci, sem utilizar recursão

programa 8.6 

def fatorial (n): # Função fatorial com parâmetro n 
    print(f'Calculando o fatorial de {n}') # printa calculando o fatorial do valor que for passado como parâmetro
    if n == 0 or n ==1: # se o valor for igual a 0 ou for igual a 1
        print(f'Fatorial de {n} = 1') # printa o fatorial de '0' ou '1' é igual a 1 e retorna 1
        return 1
    else: # se não
        fat = n * fatorial (n-1) # variavel fat recebe o valor de parêmtro vezes 1 anterior (no caso o fatorial de 5) fat = 5 * (5-1)
        print(f'Fatorial de {n} = {fat}') # printa  
    return fat # retorna o fat

fatorial(5)
'''
def fatorial (n): # Função fatorial com parâmetro n 
    print(f'Calculando o fatorial de {n}') # printa calculando o fatorial do valor que for passado como parâmetro
    if n == 0 or n ==1: # se o valor for igual a 0 ou for igual a 1
        print(f'Fatorial de {n} = 1') # printa o fatorial de '0' ou '1' é igual a 1 e retorna 1
        return 1
    else: # se não
        fat = n * fatorial (n-1) # variavel fat recebe o valor de parêmtro vezes 1 anterior (no caso o fatorial de 5) fat = 5 * (5-1)
        print(f'Fatorial de {n} = {fat}') # printa  
    return fat # retorna o fat

fatorial(5)