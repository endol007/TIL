import sys

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(a)):
    for j in range(0, len(a[i])):
        if j == 0:
            a[i][j] = a[i-1][0] + a[i][j]
        elif j == len(a[i])-1:
            a[i][j] = a[i-1][-1] + a[i][j]
        else:
            a[i][j] = max(a[i-1][j-1], a[i-1][j]) + a[i][j]
print(max(a[n-1]))