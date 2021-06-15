import sys

T = int(sys.stdin.readline())


def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


for i in range(T):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    c = gcd(a, b)
    print(int(a*b/c))

