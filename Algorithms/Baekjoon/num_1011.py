import math

test_case = int(input())

for num in range(test_case):
    x, y = map(int, input().split())
    distance = y - x
    count = 0

    num = math.floor(math.sqrt(distance))
    num_sq = num ** 2
    increase_num = math.sqrt(num_sq)

    if distance > num_sq + increase_num:
        count = 2 * num + 1
    elif distance > num_sq and distance <= num_sq + increase_num:
        count = 2 * num
    elif distance == num_sq:
        count = 2 * num -1

    if distance < 4:
        count = distance

    print(count)





# 1차이             1
# 2차이            1 1
# 3차이           1 1 1
# 4차이           1 2 1
# 5차이          1 2 1 1
# 6차이          1 2 2 1
# 7차이         1 2 2 1 1
# 8차이         1 2 2 2 1
# 9차이         1 2 3 2 1
# 10차이       1 2 3 2 1 1
# 11차이       1 2 3 2 2 1
# 12차이       1 2 3 3 2 1
# 13차이      1 2 3 3 2 1 1
# 14차이      1 2 3 3 2 2 1
# 15차이      1 2 3 3 3 2 1
# 16차이      1 2 3 4 3 2 1
# 17차이     1 2 3 4 3 2 1 1
# 18차이     1 2 3 4 3 2 2 1
# 19차이     1 2 3 4 3 3 2 1
# 20차이     1 2 3 4 4 3 2 1
# 21차이    1 2 3 4 4 3 2 1 1
# 22차이    1 2 3 4 4 3 2 2 1
# 23차이    1 2 3 4 4 3 3 2 1
# 24차이    1 2 3 4 4 4 3 2 1
# 25차이    1 2 3 4 5 4 3 2 1
# 26차이   1 2 3 4 5 4 3 2 1 1