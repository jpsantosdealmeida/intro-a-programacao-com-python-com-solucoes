# Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.

# Exemplo O rato -> {'O':1,'r':1,'a':1,'t':1,'o':1}
dic = {}
tabela = []
palavra = input('Digite uma frase ou palavra: ')
caractere = list(palavra)
'''
for indice,letra in enumerate(caractere):
    dic[letra] = indice # estou usando enumarate

'''
for letra in caractere:
    dic[letra] = 1
print(dic)
