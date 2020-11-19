
def check_palindrome(n):
    s = str(n)
    l = len(s) - 1
    i = 0

    ret = True
    while i < l:
        ret &= s[i] == s[l]
        i +=1
        l -= 1
    return ret

def p4():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if check_palindrome(num) and num > max:
                max = num
    return max

print(p4())