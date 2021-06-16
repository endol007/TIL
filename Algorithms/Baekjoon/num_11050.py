from math import factorial

n, k = map(int, input().split())
coefficient = factorial(n) // (factorial(k) * factorial(n-k))
    
print(coefficient)