import sys
t = int(sys.stdin.readline())

sum = {
}
def DP(n, sum_memo):
    rgb_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    if n == 1:
        sum_memo[1] = min(rgb_list[0])
        return sum_memo[1]
    if n == 2:
        if min(rgb_list[0][0]) == sum_memo[1]:
            sum_memo[2] == min(rgb_list[1][1], rgb_list[1][2])
        elif min(rgb_list[0][1]) == sum_memo[1]:
            sum_memo[2] == min(rgb_list[1][0], rgb_list[1][2])
        else:
            sum_memo[2] == min(rgb_list[1][0], rgb_list[1][1])

    # if n in sum_memo:
    #     return sum_memo[n]
    #
    # sum_memo = min(rgb_list[n-1]) + min(rgb_list[n-2])
    return sum_memo[n]



DP(t, sum)
