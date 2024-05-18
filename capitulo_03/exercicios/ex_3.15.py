# Quantidade de cigarros fumado por dia, quantos anos ele(ela) já fumou. cada cigarro - 10 min de vida. 
# Calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros_fumados_por_dia = int(input('Quantidade de cigarros fumado por dia: '))

anos_como_fumante = int(input('Fuma a quanto tempo? ')) * 365

print(f'{anos_como_fumante} dias como fumante\nDias de vida que irá perder {((cigarros_fumados_por_dia*10)* anos_como_fumante)/60:2f} dias ')