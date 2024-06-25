def pesquise(lista, valor):  # Função pesquisa com o parâmetro de lista e valor a ser procurado
    for x, e in enumerate(lista):  # Para cada x, e in enumere(lista)
        if e == valor:  # Se o valor dentro da lista for igual ao valor que passei como pâmetro
            return x  # Retorna o índice dele
    return None # Observa que o none está fora do For!! se não não vai funcionar


ids = [1, 2, 14, 22, 12] # Nome da lista e a lista 
print(pesquise(ids, 12)) # Printe onde eu chamo a função pesquise e passo o nome da lista,valor que quero procurar para ver se retorna o índice

