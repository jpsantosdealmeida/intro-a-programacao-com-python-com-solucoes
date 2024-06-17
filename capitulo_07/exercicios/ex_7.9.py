'''
Modifique o jogo da forca para utilizar listas de strings para desenhar o boneco da forca. Você pode utilizar uma lista
para cada linha e organizá-las em uma lista de listas. Em veze de controlar quando imprimir cada parte, desenhe
nessas listas,substituindo o elemento a desenha
'''

# Solicita a palavra secreta
palavra = input("Digite a palavra secreta: ").lower().strip()
for x in range(100):
    print()  # Limpa a tela imprimindo 100 linhas em branco

digitadas = []  # Lista para armazenar letras já digitadas
acertos = []  # Lista para armazenar letras acertadas
erros = 0  # Contador de erros
linha1 = [" ", " ", " ", " ", " "]
linha2 = [" ", " ", " ", " ", " "]
linha3 = [" ", " ", " ", " ", " "]
linha4 = [" ", " ", " ", " ", " "]
linha5 = [" ", " ", " ", " ", " "]
desenho = [linha1, linha2, linha3, linha4, linha5]
'''
IMAGINA UMA MATRIZ
             0    1    2    3    4
0 linha1 = [" ", " ", " ", " ", " "]    
1 linha2 = [" ", " ", " ", " ", " "]
2 linha3 = [" ", " ", " ", " ", " "]
3 linha4 = [" ", " ", " ", " ", " "]
4 linha5 = [" ", " ", " ", " ", " "]

'''

for linha in desenho:
    print(''.join(linha))

while True:
    senha = ""
    for letra in palavra:
        # Monta a palavra com letras acertadas e sublinhados
        senha += letra if letra in acertos else "_"
    print(senha)

    if senha == palavra:
        print("Você acertou!")  # Verifica se a palavra foi adivinhada
        break

    # Solicita uma letra do usuário
    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        # Verifica se a letra já foi tentada
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa  # Adiciona a letra à lista de letras digitadas

    if tentativa in palavra:
        acertos += tentativa  # Adiciona a letra à lista de acertos se estiver na palavra
    else:
        erros += 1  # Incrementa o contador de erros
        print("Você errou!")

    # Desenha o boneco da forca baseado no número de erros

        if erros >= 1:
            desenho[1][2] = 'O'
        if erros == 2:
            desenho[2][2] = '|'
        elif erros == 3:
            desenho[2][1] = '\\'
        elif erros == 4:
            desenho[2][3] = '/'
        elif erros == 5:
            desenho[3][1] = '/'
        elif erros == 6:
            desenho[3][3] = '\\ '

        for linha in desenho:
            print(''.join(linha))

        if erros == 6:
            print("Enforcado!")  # Verifica se o jogador perdeu
            print(f'A palavra secreta é: {palavra}')
            break
