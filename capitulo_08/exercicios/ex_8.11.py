'''
Escreva um função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. 
Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo,e falso, caso contrário.
'''

def validacao_var(palavra,min,max):
    variavel = len(palavra)
    if variavel >= min and variavel <= max:
        return True
    else:
        return False
print(validacao_var('tesd123123123aae',0,10))