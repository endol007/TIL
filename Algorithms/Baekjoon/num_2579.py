n = int(input())

s_number = {
    1: 0
}
for i in range(1, n+1):
    s = int(input())
    s_number[i] = s

def up_stairs(number, n):
    if n in number:
        return number
