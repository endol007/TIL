T = int(input())


for i in range(1, T+1):
    result_sum = i + sum(map(int, str(i)))
    if result_sum == T:
        print(i)
        break
    if i == T:
        print(0)





