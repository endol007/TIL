n, m = map(int, input().split())

numbers = list(map(int, input().split()))
b = len(numbers)
sum = 0


for i in range(0, b-2):
    for j in range(i+1, b-1):
        for k in range(j+1, b):
            if numbers[i] + numbers[j] + numbers[k] > m:
                continue
            else:
                sum = max(sum, numbers[i] + numbers[j] +numbers[k])
print(sum)
