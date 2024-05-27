# Dicionários funcionam com {} chaves.
# em um dicionário temos as chaves e os valores
# O objetivo do dicionário é armazenar informações com um rótulo para fácil acesso

tabela = {'alface': 1.0,'tomate':2.50}
#nome dicionário = {chave : valor}
print(tabela.keys()) # chaves, retorna alface e tomate
print(tabela.values()) # retorna os valores das chaves

print('manga' in tabela) # Retorna falso pois manga não está na tabela

# para apagar uma chave utilizamos del

del tabela['alface']
print(tabela)

# Se seus dados precisa preservar a ordem de inserção, como em pilhas ou listas, utilize listas

# para adicionar item
tabela['banana'] = 2.0
print(tabela)