# Modifique o programa sem utilizar a variável achou
'''
L = [10,15,20,25,28]
p = int(input('Digite o valor a procurar na lista: '))
achou = False
x = 0

while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado')'''

lista = [1,2,3,4,5]
p = int(input('Digite o valor a procurar na lista: '))
x = 0

while x < len(lista):
    if lista[x] == p:
        print(f'{p} achado na posição {x}')
        break
    x+=1
else:
    print(f'{p} não encontrado')
    novo = input(f'Gostaria de adicionar {p} a lista?(S/N): ')
    if novo == 'S':
        lista.append(p)
        print(f'Lista: {lista}')
    else:
        print('Obrigado por utilizar o programa de pesquisa do João')
