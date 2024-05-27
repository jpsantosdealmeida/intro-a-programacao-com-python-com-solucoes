# Já vimos sobre strings nos capitulos anteriores

# podemos usar >,<,^ para alinhas os valores a direita,esquerda e centro!

preco = 5.20
print(f'Preço: R$ {preco:5.2f}')
print(f'Preço: R$ {preco:<10.2f}!')
print(f'Preço: R$ {preco:>10.2f}!')
print(f'Preço: R$ {preco:^10.2f}!')

# Podemos especificar quais caracteres a preencher os espaços em branco

# podemos também alinha a direita ou esquerda
print(f'Preço: R$ {preco:x^10.2f}')

# podemos declarar funções dentro da f string

x = 5.1
print(type(x))  # Atuamente o tipo é float
print(f'Inteiro: {int(x)}')

# Podemos realizar operações matemáticas
print(f'Preço: R$ {preco * 10:5.2f}')

# A f string funcionam com strings de multiplas linhas,utilizando aspas triplas com f

print(f'''
O preço do produto é R$ {preco:5.2f}\ne pode ser encontrado na loja do ramo.
''')
