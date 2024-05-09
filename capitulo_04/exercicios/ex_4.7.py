categoria = int(input('Insira a categoria: '))
preco = 0
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
print(f'O preço do produto é R$ {preco:6.2f}')