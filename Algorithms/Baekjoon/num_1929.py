import math
a, m = map(int, input().split())

def prime_list(n):
    sieve = [True] * (n+1)

    m = int(math.sqrt(n+1))
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(2,n+1) if sieve[i] == True]


n = prime_list(m)
for i in n:
    if i >= a:
        print(i)


