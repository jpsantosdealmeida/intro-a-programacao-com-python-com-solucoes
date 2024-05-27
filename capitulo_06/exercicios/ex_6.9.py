# Modifique o exemplo para procurar 2 valores. Em vez de apenas p, leia outro valor v que também será procurado.
# Na impressão, indique qual dos 2 valores foi achado primeiro.

lista = [1,2,3,4,5]
p = int(input('Digite o 1° valor a procurar na lista: '))
v = int(input('Digite o 2° valor a procurar na lista: '))
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

x = 0
while x < len(lista):
    if lista[x] == v:
        print(f'{v} achado na posição {x}')
        break
    x+= 1
else:
    print(f'{v} não encontrado')
    novo = input(f'Gostaria de adicionar {v} a lista?(S/N): ')
    if novo == 'S':
        lista.append(v)
        print(f'Lista: {lista}')
    else:
        print('Obrigado por utilizar o programa de pesquisa do João')



    
    