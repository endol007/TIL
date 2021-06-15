import sys

T = int(sys.stdin.readline())

for i in range(T):
    string = sys.stdin.readline()
    vps = list(string)
    count = 0
    for char in vps:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            print("NO")
            break
    if count > 0:
        print("NO")
    elif count == 0:
        print("YES")



