'''
Escreva um gerador capaz de gerar a sequência dos números primos.
'''

def eh_primo(n): # recebe um parâmetro n
    if n <= 1: # se n for menor ou igual 1
        return False # então não é primo
    for i in range(2, int(n**0.5) + 1): # para cada i (i = nome qualquer) no alcance de 2 até a raiz quadrada de n
        if n % i == 0: # se n for divisível por qualquer i 
            return False # não é primo
    return True

def gerador_primo(): 
    n = 2 # n começa com 2
    while True: # enquanto verdade
        if eh_primo(n): # se eh primo, se retorna true
            yield n 
        n += 1

primos = gerador_primo()
for _ in range(10):
    print(next(primos))