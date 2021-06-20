T = int(input())

for i in range(T):
    n = int(input())
    length = [0] * (101)
    length[0] = 0
    length[1] = length[2] = length[3] = 1
    length[4] = 2
    a = 5
    if n > 4:
        while True:
            length[a] = length[a-1] + length[a-5]
            if a == n:
                break
            a += 1

    print(length[n])

