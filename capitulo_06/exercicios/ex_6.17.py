# Altere o programa abaixo de modo a solicitar ao usuário o produto e a quantidade vendida.
# Verifique se o nome do produto digitado existe no dicionário, e só então efutue a baixa em estoque.
'''
estoque = {'tomate':[1000,2.30],
'alface':[500,0.45],
'batata': [2001,1.20],
'feijão':[100,1.50]}
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
print(f'Custo toal: {total:21.2f}\n')
print('Estoque:\n')
for chave,dados in estoque.items():
    print('Descrição:', chave)
    print('Quantidade:', dados[0])
    print(f'Preço: {dados[1]:6.2f}\n')
    '''
estoque = {'tomate':[1000,2.30],
'alface':[500,0.45],
'batata': [2001,1.20],
'feijão':[100,1.50]}
total = 0

while True:
    produto = input('Digite o produto vendido ("sair" para encerrar): ')
    if produto == 'sair':
        print('Vendas:\n')

    produto = estoque[produto]
    quantidade = estoque['alface'][0]
    print(produto,quantidade)
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
    break   
    quantidade = int(input(f"Digite a quantidade do {produto} vendido: "))
    venda = estoque[produto] = quantidade


print('Vendas:\n')

produto = estoque[produto]
quantidade = estoque[produto][0]
print(produto,quantidade)
preco = estoque[produto][1]
custo = preco * quantidade
print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
estoque[produto][0] -= quantidade
total += custo
print(f'Custo toal: {total:21.2f}\n')
print('Estoque:\n')
for chave,dados in estoque.items():
    print('Descrição:', chave)
    print('Quantidade:', dados[0])
    print(f'Preço: {dados[1]:6.2f}\n')
estoque = {'alface':[100,2.50]}


