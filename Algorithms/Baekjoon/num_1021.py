n, m = map(int, input().split())
count = 0



def enqueue(start, end, a):
    string = []
    for i in n:
        string.append(i)

    start = start
    end = end
    while start <= end:
        mid = (start + end) // 2
        num = 0
        for i in string:
            if i - mid > 0:
                num += i - mid
        if num >= a:
            start = mid + 1
        else:
            end = mid -1
    return end

for i in m:
    j = int(input())
    while True:
        if m == enqueue(0, n-1, j):
            count = count
        else:
            count += 1
            del string[0]







