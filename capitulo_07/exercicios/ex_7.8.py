'''
Modifique o jogo da forca de forma a utilizar uma lista de palavras
No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula:
indice = (numero * 776) % len(lista_de_palavras).
Ou seja, criamos uma lista
adicionamos palavras a essa lista
perguntamos o índice para selecionar a palavra , por exemplo, se colocarmos 10 palavras poderiamos perguntar "selecione um número de 1 a 10"

numero = int(input('Insira um número de 0 a 4: '))
indice = (numero * 776) % len(lista_de_palavras) # fui fazendo passo a passo para ir ver como ficaria , resultou nisso 
print(f'Indice: {indice}')
print(lista_de_palavras[indice])

'''

# Solicita a palavra secreta
lista_de_palavras = ["python", "java", "javascript", "ruby", "perl",'abacaxi','banana']
numero = int(input('Insira um número para selecionar a palavra: '))
indice = (numero * 776) % len(lista_de_palavras) # No caso aqui seria numero que a pessoa inserir * qualquer numero resto de divisão % do tamanha da lista
# isso garante que independente do numero vai selecionar um palavra da lista, não precisamos verificar se o numero inserido está dentro do alcance
# palavra = input("Digite a palavra secreta: ").lower().strip()
palavra = lista_de_palavras[indice]
for x in range(100):
    print()  # Limpa a tela imprimindo 100 linhas em branco

digitadas = []  # Lista para armazenar letras já digitadas
acertos = []  # Lista para armazenar letras acertadas
erros = 0  # Contador de erros

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
    print("X==:==\nX  : ")
    print("X  O " if erros >= 1 else "X")

    linha2 = ""
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " \| "
    elif erros >= 4:
        linha2 = " \|/ "
    print(f"X{linha2}")

    linha3 = ""
    if erros == 5:
        linha3 += "/"
    elif erros >= 6:
        linha3 += " / \ "
    print(f"X{linha3}")

    print("X\n===========")
    print("X\n-----------")

    if erros == 6:
        print("Enforcado!")  # Verifica se o jogador perdeu
        print(f'A palavra secreta é: {palavra}')
        break

