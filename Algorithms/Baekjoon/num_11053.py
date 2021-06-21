import sys
t = int(input())
num = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(t)]

for i in range(t):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))