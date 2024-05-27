# Modifique o programa anterior de forma a ler um número n e imprima os n primeiros números primos

print('*'*25)
print('Veficador de números primos')
print('*'*25)
n = int(input('Insira um número para verificar se o mesmo é PRIMO: '))

while True:
    n = int(input('Insira um número para verificar os primos de 2 até ele (ou um número negativo para sair): '))
    
    if n < 2:
        print('Por favor, insira um número maior que 1.')
        continue

    for num in range(2, n + 1):
        primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            print(f'{num} é primo.')
    
    outro = input('Deseja verificar outro número? (s/n): ').strip().lower()
    if outro != 's':
        break

print('Programa encerrado.')