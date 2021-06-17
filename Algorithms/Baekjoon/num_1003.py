import sys
T = int(input())

memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n <= 2:
        return 1
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


for i in range(T):
    f = int(sys.stdin.readline().rstrip())
    if f == 0:
        print("1 0")
    elif f == 1:
        print("0 1")
    else:
        print(fibo_dynamic_programming(f-1, memo), fibo_dynamic_programming(f, memo))