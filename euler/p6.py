
def p6(n=100):
    sum_squares = 0
    sum_squared = 0

    for i in range(1, n+1):
        sum_squares += i * i
        sum_squared += i

    sum_squared *= sum_squared

    return sum_squared - sum_squares

print(p6())
    