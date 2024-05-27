# Modifique o exercício anterior para ler 7 notas em vez de 5

notas = [0,0,0,0,0,0,0] # só acrescentar mais 2 elementos
soma = 0
x = 0

while x < 7: # mudar de 5 para 7
    notas[x] = float(input(f'Nota {x} :'))
    soma += notas[x]
    x +=1
x = 0
while x < 7: # mudar de 5 para 7
    print(f'Nota {x}: {notas[x]:6.2f}')
    x += 1
print(f'Média: {soma / x:5.2f}')