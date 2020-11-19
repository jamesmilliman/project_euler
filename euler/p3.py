import math


def p3(n=600851475143):
    factors = []

    while (n % 2 == 0):
        factors.append(2)
        n /= 2
    
    i = 3
    while i <= math.sqrt(n):
        while (n % i == 0):
            factors.append(i)
            n /= i
        i += 2

    if n > 2:
        factors.append(n)

    return factors

f = p3()
