"""https://projecteuler.net/problem=1"""


def p1():

    sum = 0
    for i in range(1000):
        m3 = i % 3 == 0
        m5 = i % 5 == 0
        if m3 or m5 and not (m3 and m5):
            sum += i

    return sum

if __name__ == '__main__':
    print(p1())