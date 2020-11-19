
def p5(n = 20):
    x = n
    found = False
    while True:
        found = True
        for i in range(1, n):
            if x % i != 0:
                found = False
                break
        if found:
            return x
        else:
            x += n

print(p5())