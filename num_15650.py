#조합라이브러리 이
from itertools import combinations

n, m = map(int, input().split())

C = combinations(range(1, n+1), m)
용
for i in C:
    print(' '.join(map(str, i)))


# 두번째 방법
# n, m = list(map(int, input().split()))
# s = []
#
#
# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(start, n + 1):
#         if i not in s:
#             s.append(i)
#             print(i, "i2")
#             dfs(i + 1)
#             print(s.pop())
#
# dfs(1)