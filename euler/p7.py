
def p7(n=10001):
    max = 10000*n
    temp = [True for _ in range(max)]

    for i in range(2, max):
        if temp[i]:
            for start in range(2 * i, max, i):
                temp[start] = False
    
    num = 0
    for i in range(2, max):
        if temp[i]:
            num +=1
            if num == n:
                return i
    return None

print(p7())