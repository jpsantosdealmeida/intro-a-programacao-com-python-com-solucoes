'''
Função são úteis para validar a entrada de dados

Ex deu um código que para ler um valor inteiro limitado por um valor mínimo e máximo. Esse trecho repete a entrada de dados até termos um valor válido.


while True:
    v = int(input('Dgitie um valor entre 0 e 5: ))
    if v < 0 or v > 5:
        print('Valor inválido.')
    else:
        break
        
Podemos tranformar em uma função que recebe a pergunta, valor máximo e mínimo.
def faixa_int(perg,min,max):
    while True:
        v = int(input(perg))
        if v < min or v > max:
            print(f'Valor inválido. Digite um valor entre {min} e {max}')
        else:
            return v
'''
