import sys
input = sys.stdin.readline
while True:
    string = input().rstrip()
    if string == ".":
        break
    stack = []
    count = 1
    temp = True
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            print(stack, "1")
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                count = 0
                break
        elif i == ']':
            print(stack, "2")
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                count = 0
                break
    print("yes" if count and not(stack) else "no")
