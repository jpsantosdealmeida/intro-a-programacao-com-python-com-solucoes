'''
Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(()) OK
()()(()) OK
()) Erro

Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilha-la a cada fecha parênteses.
Ao desempilhar, verifique se o topo da pilha é um abre parênteses. Se a expssão estiver correta, sua pilha estará vazia no final.
'''

'''

Pilha: Uma lista é usada como pilha para armazenar os parênteses.

Iteração sobre a Expressão: O código percorre cada caractere da expressão.

Abre Parênteses: Se o caractere é um '(', ele é adicionado à pilha.

Fecha Parênteses: Se o caractere é um ')', verifica se a pilha está vazia. Se estiver, isso indica que há um parêntese de fechamento sem um 
correspondente de abertura, retornando "Erro". Caso contrário, remove (desempilha) o topo da pilha.

Verificação Final: Após percorrer toda a expressão, verifica se a pilha está vazia. Se estiver, significa que todos os parênteses de abertura foram corretamente fechados, retornando "OK". Se não, retorna "Erro".
'''

pilha = []
expressao = input('Passa os parênteses para a pilha: ')

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) == 0:
            print('Erro')
        pilha.pop()

if len(pilha) == 0:
    print('OK')
else:
    print('Erro')
    
