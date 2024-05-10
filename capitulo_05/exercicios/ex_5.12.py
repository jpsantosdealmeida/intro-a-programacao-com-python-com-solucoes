# Altere o programa de forma a perguntar o depósito mensalmente

dep_inicial = float(input('Insira o depósito inicial: '))
taxa_juros = float(input('Insira a taxa de juros da poupança: '))
deposito = float(input('Qual o valor a depositar mensalmente: '))
mes = 1
total_ganho = 0

while mes <= 24:
    dep_inicial += deposito
    lucro = (dep_inicial * taxa_juros / 100)
    print(f'O lucro no {mes}° foi de {lucro:.2f} ')
    dep_inicial += lucro 
    total_ganho += lucro
    mes += 1
print(f'O valor total de juros acumulado  foi de {total_ganho:5.2f} {dep_inicial}')
'''
>> Analisar criticamente
tente explicar o problema para você mesmo em voz alta

Q n° 1 - Quais são os dados de entrada necessários? dep inicial, taxa juros
Q n° 2 - O que devo fazer com estes dados? porcentagem primeiro (dep inicial - (dep inicial * taxa / 100))
Q n° 3 - Quais são as restrições deste problema?
Q n° 4 - Qual é o resultado esperado? valor mes a mes de ganho e valor total
Q n° 5 - Qual a sequência de passos a ser feitas para chegar ao resultado esperado?
dep inicial
taxa mes
calcular % de ganho
condicional
retornar valor mes a mes e total
'''
