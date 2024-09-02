# Função modificada para facilitar o rastreamento

def fatorial(n):
    print(f'Calculando o fatorial de {n}')
    if n == 0 or n == 1:
        print(f'Fatorial de {n} = 1')
        return 1
    else:
        fat = n*fatorial(n-1)
        print(f'fatorial de {n} = {fat}')
        return fat
fatorial(4)