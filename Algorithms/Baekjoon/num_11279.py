import sys
T = int(sys.stdin.readline())
num = []
for i in range(T):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(num) == 0:
            print(0)
        else:
            num.sort()
            print(max(num))
            num.pop()
    else:
        num.append(x)