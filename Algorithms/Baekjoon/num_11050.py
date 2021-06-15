import sys

n, k = sys.stdin.readline().split()


def number(a):
    return number(a-1)*number(a-2)

print(number(int(n)))