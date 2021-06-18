# 백트레킹의 대표적 예시문제라고 한다
# 백트레킹은 가지치기 방식으로 해가 더 나올거같지않으면 탐색을 스탑하고 다음으로 넘어가는걸 말
def adjacent(x):
    for i in range(x):   # 인덱스가 행의 값이고 row[index]의 값이 열의 값이다.
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result

    if x == n:
        result +=1
    else:
        for j in range(n):
            row[x] = j
            if adjacent(x):
                dfs(x+1)



n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)