import sys
input = sys.stdin.readline

T, N = map(int, input().split())
trees = list(map(int, input().split()))
n, m = 0 , max(trees)

def find_trees_length(start, end):
    start = start
    end = end
    while start <= end:
        mid = (start + end) // 2
        num = 0
        for i in trees:
            if i - mid > 0:
                num += i - mid
        if num >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(find_trees_length(n, m))
