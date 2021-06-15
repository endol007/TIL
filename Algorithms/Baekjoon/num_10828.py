import sys

test = int(sys.stdin.readline())
stack = []
for i in range(test):
    string = sys.stdin.readline().split()
    if "push" in string:
        stack.append(string[1])
    elif "top" in string:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif "size" in string:
        print(len(stack))
    elif "empty" in string:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "pop" in string:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())



