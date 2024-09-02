'''Reescreva a fuynção de cálculo da sequência de Fibonacci, sem utilizar recursão.
Fibonacci
def fib (n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
'''

def fib(n):
    if n <= 1:
        return n 
    else:
        while n > 1:
            n1 = n-1
            n2 = n-2
            vlfinal = n1 - n2
        return vlfinal
    
print(fib(5))