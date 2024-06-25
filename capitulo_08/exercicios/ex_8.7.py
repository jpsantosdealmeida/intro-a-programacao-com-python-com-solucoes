'''
Defina um função recursiva que calcule o maior divisor comum (M.D.C) entre dois números a e b, em que a > b.

mdc(a,b) = | a
           | mdc(b,a-b [a])   b = 0 , a > b
                        b

                        
'''

def mdc(a,b):
    while b != 0:
        r = a - b
        a = b
        b = r
