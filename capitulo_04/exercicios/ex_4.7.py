categoria = int(input('Insira a categoria: '))
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
                else:
                    print('Categoria inválida, digite um valor entre 1 e 5 !')
                    preco = 0
print(f'O preço do produto é R$ {preco:6.2f}')
# Verifique o programa abaixo e compare seu resultado ao apresentado na tabela
'''
CATEGORIA | LINHAS EXECUTADAS
    1     | 1,2,3,19
    2     | 1,2,4,5,6,19
    3     | 1,2,4,5,7,8,9,19
    4     | 1,2,4,5,7,8,10,11,12,19
    5     | 1,2,4,5,7,8,10,11,13,14,15,19
 OUTRAS   | 1,2,4,5,7,8,10,11,13,14,16,17,18,19
'''

