import sys
n, c = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()

answer = 0
def binary_search(start, end):
    if start > end:
        return
    mid = (start + end) // 2
    cnt = 1
    target = 0

    for i in range(n):
        if a[i] >= a[target] + mid:
            cnt += 1
            target = i
    if cnt >= c:
        global answer
        answer = max(answer, mid)
        binary_search(mid + 1, end)
    else:
        binary_search(start, mid -1)

binary_search(1, (a[-1] - a[0])//(c-1)+1)
print(str(answer))