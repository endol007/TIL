import sys

n, m = map(int, sys.stdin.readline().split())

t = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

a = []
b = []
for i in range(m):
    for j in range(n):
        if t[i][j] == 1:
            a.append(i)
            b.append(j)



