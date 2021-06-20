n, k = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

count = 0
while k:
    for i in reversed(range(n)):
        if k // money[i] > 0:
            count = count + k // money[i]
            k = k - (k // money[i])*money[i]
    if k == 0:
        break

print(count)
