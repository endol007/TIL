import sys
n = int(sys.stdin.readline())

paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0


def cut_paper(x, y, n):
    global blue, white
    check = paper[x][y]
    for j in range(x, x + n):
        for k in range(y, y+n):
            if check != paper[j][k]:
                cut_paper(x, y, n//2)
                cut_paper(x + n//2, y, n//2)
                cut_paper(x, y + n//2, n//2)
                cut_paper(x + n//2, y + n//2, n//2)
                return
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return


cut_paper(0, 0, n)
print(white)
print(blue)
