T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance_x_y = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    rs = r1 + r2
    rm = abs(r1-r2)
    if distance_x_y == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance_x_y == rs or distance_x_y == rm:
            print(1)
        elif rs > distance_x_y > rm:
            print(2)
        else:
            print(0)


