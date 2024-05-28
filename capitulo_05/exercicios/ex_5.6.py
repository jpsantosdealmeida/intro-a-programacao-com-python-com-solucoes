#  Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4
print('-' * 15)
print('    Tabuada')
print('-' * 15)

n = int(input('Tabuada do : '))
x = 1
while x <= 10:
    print(f'{x} x {n} = {x*n}') 
    x +=1