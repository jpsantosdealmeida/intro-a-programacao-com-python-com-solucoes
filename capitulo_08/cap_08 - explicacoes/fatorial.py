def fatorial(n):
    fat = 1 # Definimos fatorial = 1
    while n > 1: # Enquanto o valor que passamos como parâmetro for maior que 1
        fat *= n # o Fatorial vai ser = a ele x parâmetro (EX: fat = 1*5) agora fat vale 5
        # O próximo vai ser fat = 5 * 4 = 20 fat agora vale 20, proximo é fat = 20 * 3 e assim até chegar a 1
        n-=1 # Aqui retira 1 do numero passado como parâmetro
    return fat

print(fatorial(5))