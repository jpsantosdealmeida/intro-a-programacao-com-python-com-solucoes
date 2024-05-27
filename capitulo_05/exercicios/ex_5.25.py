# Escreva um programa que calcule a raíz quadrada de um número 
# Utilize o método de newton para obter um resultado aproximado
# Sendo o n o número a obter a raíz quadrada, conside a base b=2
# Calcule p usando a fórmula p = (b+(n/b))/2.
# Agora calcule o quadrado de p, a cada passo faça b=p e
# recalcule p usando a fórmula apresentada.
# Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0.0001.

n = int(input('Insira o número que deseja calcular a raíz: '))
# b ou base = 2
b = 2
limite = 0.0001

while True:
    p = (b+(n/b))/2
    if (p**2 - n) < limite:
        print(f'A raíz quadrada de {n} é  aproximadamente {p:5.2f}')
        break
    b = p
