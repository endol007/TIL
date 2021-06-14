def self_number(n):
    n = n + sum(map(int,str(n)))

    return n

a = [0]*10001

for i in range(1, 10001):
    a[i] = self_number(i)

for i in range(1, 10001):
    if i not in a:
        print(i)