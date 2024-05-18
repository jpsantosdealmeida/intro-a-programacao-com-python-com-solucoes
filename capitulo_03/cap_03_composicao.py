# Composição
x = 15
idade = 24

# modelo antigo
print('joao tem %d anos'% x)

"""
%d --- números inteiros
%s --- Strings
%f --- números defimais
"""
print('%d'% idade)

print('%04d' % idade)

print('%4d' % idade)


# modelo . format
print('joão tem {} anos'.format(x))

#modelo f string
print(f'joao tem {x} anos')