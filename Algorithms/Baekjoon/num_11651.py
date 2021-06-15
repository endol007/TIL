N = int(input())
point = []
for i in range(N):
    [x, y] = map(int, input().split())
    rev = [y, x]
    point.append(rev)

point = sorted(point)

for i in range(N):
    print(point[i][1], point[i][0])
