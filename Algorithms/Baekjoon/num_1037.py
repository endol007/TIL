num = int(input())

a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_min * a_max)
