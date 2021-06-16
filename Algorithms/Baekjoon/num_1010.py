from math import factorial

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n)*factorial((m - n)))
    print(bridge)