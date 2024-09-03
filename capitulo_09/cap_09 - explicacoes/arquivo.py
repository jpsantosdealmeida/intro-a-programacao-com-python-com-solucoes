'''
>>> O que é um arquivo? É um espaço no disco onde podemos ler e gravar informações. O própio SO gerencia a área.

No python para acessar um arquivos precisamos abri-lo, informar o nome, com o nome do diretório (caso ele não estiver na mesma pasta do .py)
e dizer a operação que queremos realizar.

No python utilizamos a FUNÇÃO open() junto com a operação a realizar.

- r = leitura
- w = escrita,apaga conteudo se já existir
- a = escrita,preserva o conteúdo se já existir
- b = modo binário
- + = atualização (leitura e escrita)

Os módulos podem ser combinados 'r+','r+w' etc...

Ao trabalhar com arquivo devemos sempre fazer um ciclo: abrir, ler ou escrever,fechar

abir com OPEN
READ ou WRITE
CLOSE

'''
'''
arquivo = open('teste.txt','w') # variavel arquivos é igual a um open
for linha in range(1,101): # Para cada linha entre 0 e 100
    arquivo.write(f'{linha}\n') # escreva o valor ou número da linha
'''

# observa-se que se escrevermos nesse arquivo e rodar o código novamente, o que foi escrito será perdido, pois o código gera um outro arquivo

arquivo = open('teste.txt','r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# para cada linha no arquivo, leia todas elas,printa e depois fecha o arquivo