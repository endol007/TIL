input = 100
memo = {
    1: 1,
    2: 1
}

def fibo_recursion(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_recursion(n-1, fibo_memo) + fibo_recursion(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

print(fibo_recursion(input, memo))  # 6765