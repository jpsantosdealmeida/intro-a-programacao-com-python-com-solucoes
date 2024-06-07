'''
>>> POSICIONAMENTO DE STRINGS

Python tem métodos para deixar a apresentação das strings mais interessantes

CENTER - centraliza a string em um número de posições passado
obs: Se alem do tamanho você passar o caractere de preenchimento, este será utilizado no lugar de espaços em branco

LJUST - Se deseja completar espaços à esquerda

RJUST - Se deseja completar espaços à direita

>>> QUEBRA OU SEPARAÇÃO DE STRINGS

SPLIT - quebra uma linha a partir de uma linha a partir de um caractere passado

>>> SUBSTITUIÇÃO DE STRINGS

REPLACE - Para substituir trechos de strings por outros (string a substituir, conteudo que substituirá, OPCIONAL( quantas vezes substituirá))

>>> REMOÇÃO DE ESPAÇOS EM BRANCO

STRIP - Remover espaços em branco do início ou fim da string

LSTRIP - Remover caracteres em branco a esquerda

RSTRIP - Remover caracteres em branco a direira

OBS: Se você passar um parâmetro no método, este sera o caractere a remover

>>> VALIDAÇÃO POR TIPO DE CONTEÚDO

Strings podem ter seu conteúdo anaisado, esses métodos verificam se os caracteres são letra, números ou combinação deles.

ISALPHA - Retorna True apenas se todos os caracteres são letras
OBS: Retorna falso se algum outro tipo de caractere for encontrada ou se a string estiver vazia

ISALNUM - Retorna True se a string não estiver vazia, e se os caracteres são letra e/ou números
OBS: Se a string contiver outros tipos de caracteres, como espaços, vírgula, exclamação etc.. retorna False

ISDIGIT - Retorna True se o valor consiste em número
OBS: Se a string estiver vazia, conter espaços,pontos vírgulas ou sinais retorna False

ISUPPER - Verifica se todos os caracteres são maíusculos

ISLOWER - Verifica se todos os caracteres são minúsculos


>>> ENTRE OUTRAS MANIPULAÇÕES 

'''
s = 'tigre'
print('CENTER\n'.center(50))
print(f'x{s.center(10)}x > CENTRALIZANDO COM 10 ESPAÇOS')
print(f'x{s.center(10, '-')
          }x > CENTRALIZANDO COM 10 ESPAÇOS E PREENCHENDO OS ESPAÇOS COM -\n')
print('LJUST\n'.center(50))
print(f'{s.ljust(20)} > AJUSTE A ESQUERDA COM 20 ESPAÇOS')
print(f'{s.ljust(20, '.')} > AJUSTE A ESQUERDA COM 20 ESPAÇOS PREENCHIDOS COM .\n')
print('RJUST\n'.center(50))
print(f'{s.rjust(20)} > AJUSTE A DIREITA COM 20 ESPAÇOS')
print(f'{s.rjust(20, '.')} > AJUSTE A DIREITA COM 20 ESPAÇOS PREENCHIDOS COM .\n')

frase = 'O rato, roeu, a roupa'
print('SPLIT\n'.center(50))
print(f'{frase.split()} > SEPAROU EM CADA FRASE, (NÃO COLOQUEI NENHUM PARÂMETRO)\n')
print(f'{frase.split(',')
         } > SEPAROU EM 3 POIS PASSEI O PARÊMETRO PARA DIVIDIR NAS VÍRGULAS\n')
print('REPLACE\n'.center(50))
print(f'{frase.replace('rato', 'gato')} > SUBSTITUIU A FRASE RATO POR GATO\n')

t1 = '         OLA MUNDO        '
t2 = '///------OLA MUNDO-----///'
print('STRIP\n'.center(50))
print(f'{t1} > SEM O MÉTODO STRIP')
print(f'{t2} > SEM O MÉTODO STRIP\n')
print(f'{t1.strip()} > REMOVI OS ESPAÇOS EM BRANCO DA VARIÁVEL t')
print(f'{t2.strip('/')} > REMOVI SOMENTE AS / ')
print(f'{t1.lstrip()} > REMOVI SOMENTE OS ESPAÇOS EM BRANCO A ESQUERDA')
print(f'{t1.rstrip()} > REMOVI SOMENTE OS ESPAÇOS EM BRANCO A DIREITA\n')

print('ISALPHA\n'.center(50))
