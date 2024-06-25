def soma(lista):
    total = 0
    for numero in lista:  # Para cada numero dentro da lista
        total += numero  # A variável total recebe ela mais o número, vai fazer isso para toda a lista
    return total  # Retorna o total


def media(lista):
    return soma(lista) / len(lista)


uma_lista_qualquer = [10, 20, 30, 40, 50]  # Soma = 150
# uma_listaqualquer = [ 0  1  2  3  4] # média = 150 / 5 ou seja o total que é 150 divido pelo seu tamanho que é 5
print(media(uma_lista_qualquer))
