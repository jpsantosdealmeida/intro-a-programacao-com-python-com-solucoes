'''
Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar 
e alternar entre os jogadores. A cada jogada, verifique se a 
posição está livre. Verifique também quando um jogador venceu a partida. 
Um jogo da velha pode ser visto com uma lista de 3 elementos, na qual cada elemento
é outra lista, também com 3 elementos.

Exemplo do jogo
X | 0 |  
--+---+--
  | X | X
--+---+--
  |   | 

Em cada posição pode ser vista com um número. Confira a seguir um exemplo da posições mapeadas para a mesma posição de seu teclado númerico.

7 | 8 | 9
--+---+--
4 | 5 | 6
--+---+--
1 | 2 | 3
'''

# Inicializa o tabuleiro vazio
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define os jogadores e o símbolo de cada um
jogadores = ["X", "O"]
simbolos = {1: "X", 2: "O"}

# Define a variável para controlar de quem é a vez
vez = 0

# Mostra o tabuleiro inicial
print("Jogo da Velha\n")
for linha in tabuleiro:
    print("|".join(linha))
    print("-" * 5)

# Loop principal do jogo
for _ in range(9):  # O jogo tem no máximo 9 jogadas
    # Pede a jogada do jogador atual
    jogada = int(input(f"\nJogador {jogadores[vez]}, faça sua jogada (1-9): ")) - 1

    # Converte a jogada em linha e coluna
    linha = jogada // 3
    coluna = jogada % 3

    # Verifica se a posição está ocupada
    if tabuleiro[linha][coluna] != " ":
        print("Posição já ocupada. Escolha outra.")
        continue

    # Faz a jogada
    tabuleiro[linha][coluna] = simbolos[vez + 1]

    # Mostra o tabuleiro atualizado
    print("\nTabuleiro atualizado:")
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

    # Verifica se houve um vencedor
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " " or \
                tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            print(f"\nJogador {jogadores[vez]} venceu!")
            break
    else:
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " " or \
                tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            print(f"\nJogador {jogadores[vez]} venceu!")
            break

    # Muda para o próximo jogador
    vez = (vez + 1) % 2

    # Se todas as posições estiverem preenchidas e não houver vencedor, é empate
    if all(all(pos != " " for pos in linha) for linha in tabuleiro):
        print("\nEmpate!")
        break
