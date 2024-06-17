# JOGO DA FORCA
# Solicita a palavra secreta
palavra = input("Digite a palavra secreta: ").lower().strip()
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
        break
