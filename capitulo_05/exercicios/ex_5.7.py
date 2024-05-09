# Tabuada
# modifique o programa a fim que o usuário digite o início e o fim da tabuada
print('-' * 15)
print('    Tabuada')
print('-' * 15)

n = int(input('Tabuada do (início) : '))
f = int(input('até (fim)'))
x = 1
while x <= f:
    print(f'{x} x {n} = {x*n}') 
    x +=1