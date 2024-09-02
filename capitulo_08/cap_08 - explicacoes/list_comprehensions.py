'''
Uma forma simples de criar lista é usando list comprehensions, capaz de especificar como os elementos de uma lista devem ser gerados.

L = [x for x in range(10)] 
saída = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

outro exemplo

Z = [x * 2 for in [0,1,2,3]]
saída = [0,2,4,6]

podemos ler assim, retorne uma lista em que cada elemento é igual ao dobro d elemento x da lista passada como prametro, ou,
retorne assim o dobro de x para x em [0,1,2,3].

Z = [i.upper() for i in 'abcdef'] # elemento maiusculo para cada elemento dentro da lista abcdef
'''
L = [x for x in range(10)]
print(L)