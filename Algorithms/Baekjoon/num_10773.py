import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))

