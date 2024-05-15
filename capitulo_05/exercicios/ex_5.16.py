# Execute o programa 5.1 de cédulas

valor = int(input('Digite o valor a pagar: ')) # 245
cedulas = 0
atual = 50
apagar = valor  # 245

while True:
    if atual <= apagar:  # se 50 for menor(<=) ou igual a 245. isso é TRUE
        apagar -= atual # Apagar recebe 245 - 50                                # Esse laço vai se repetir 4 vezes
        cedulas += 1 # Cedulas ganha 1
    else:
        if cedulas > 0:
            print(f'{cedulas} cédula(s) de R$ {atual}')
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

# ENTENDI PORRRAAAAA
'''
A lógica é a seguinte , no primeiro IF o atual é igual a 50, vamos dizer que o apagar vai ser 245
e ele compara, olha, 50 ele é menor ou igual a 245, isso retorna Verdadeiro, logo ele tira do apagar(245) 50 e ganha 1 cedula
e compra novamente , olha 50 é menor ou igual a 195, retorna Verdadeio, logo ele tira 50 do apagar(195) e ganha mais 1 cedula
e compara novamente, olha 50 é menor ou igual a 145, retorna Verdadeiro, logo ele tira 50 do apagar (145) e ganha mais 1 cedula
e compara novamente, olha 50 e menor ou igual a 95, retorna Verdadeiro, logo ele tira 50 do apagar(95) e ganha mais 1 cedula
e compara novamente, olha 50 é menor ou igual a 45, isso retorna Falso e nosso while é enquando verdade
ele cai no Else, se o apagar for 0, termina o programa, se o apagar for 50, agora ele vai ser 20, e retorna la para as comparações
olha, 20 é menor ou igual a 45, isso retorna verdadeiro, logo ele tira 20** do apagar(45) e ganha mais 1 cedula de 20
faz isso denovo e retorna verdadeiro
depois , olha 20 é menor ou igual a 5, da Falso, vai para o else , e compara , o atual é 50? não , o atual é 20? True, então agora ele é 10
volta na no primeiro laço e da falso pois 10 é maior que 5,
ele retorna para o else e compara , o atual é 10? True, então agora ele é 5
e retorna lá para o primeiro laço enquanto verdade , 5 é menor ou igual a 5, isso é True, 5 é menor ou igual a 0, Falso, ele cai no else e verifica
o apagar é 0? vai dar True e ele termina o programa
'''