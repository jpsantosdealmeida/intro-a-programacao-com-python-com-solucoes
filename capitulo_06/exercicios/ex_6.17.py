# Altere o programa abaixo de modo a solicitar ao usuário o produto e a quantidade vendida.
# Verifique se o nome do produto digitado existe no dicionário, e só então efutue a baixa em estoque.

'''

estoque = {'tomate': [1000, 2.30],
           'alface': [500, 0.45],
           'batata': [2001, 1.20],
           'feijão': [100, 1.50]}
venda = [['tomate',5],['batata',10],['alface',5]]
total = 0
print('Vendas:\n')
for operacao in venda:
    produto,quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo total: {total:23.2f}\n')
print('Estoque:\n')
for chave,dados in estoque.items():
    print('Descrição:', chave)
    print('Quantidade:', dados[0])
    print(f'Preço: {dados[1]:6.2f}\n')
'''

estoque = {'tomate': [1000, 2.30],
           'alface': [500, 0.45],
           'batata': [2001, 1.20],
           'feijão': [100, 1.50]}
venda = []

produto = input('Insira o produto da venda: ')
quantidade = int(input('Insira a quantidade vendida: '))
preco = estoque[produto][1]
total = 0
if produto in estoque:
    if quantidade <= estoque[produto][0]:
        print('Vendas:\n')
        custo = preco * quantidade
        print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
        estoque[produto][0] -= quantidade
        total += custo
print(f'Custo total: {total:23.2f}\n')
print('Estoque:\n')
for chave,dados in estoque.items():
    print('Descrição:', chave)
    print('Quantidade:', dados[0])
    print(f'Preço: {dados[1]:6.2f}\n')


'''
# venda = [['tomate',5],['batata',10],['alface',5]]
# variavel=[[    0     ],[     1     ],[     2    ]]
# dentro =[['[0]', [1]],['[0]', [1] ],['[0]', [1] ]

tabela = {'alface': [5, 4.50],
          'tomate': [10, 5.0],
          'batata': [15, 2.50]}

venda = [['alface', 2,4.50], ['batata', 5,2.50]]
# o tamanho é 0       e      1

# aqui estou falando pega o primeiro indice e o primeiro elemento dentro dessa lista que é o alface, o 2 é o 1
for operacao in venda:
    produto,quantidade,preco = operacao
    print(f'Produto: {produto}')
    print(f'Quantidade: {quantidade}')
    print(f'Preço: R$ {preco:5.2f}')
'''
