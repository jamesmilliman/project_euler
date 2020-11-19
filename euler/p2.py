"""https://projecteuler.net/problem=2"""


def generate_fibs(n=4000000):
    fibs = [0, 1]
    while True:
        new = fibs[-2] + fibs[-1]
        if new > n:
            return fibs
        fibs.append(new)

def p2():

    sum = 0
    fibs = generate_fibs()
    for each in fibs:
        if each % 2 == 0:
            sum += each

    return sum

if __name__ == '__main__':
    print(p2())