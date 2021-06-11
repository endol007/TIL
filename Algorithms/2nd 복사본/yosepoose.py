def josephus_problem(n, k):
    result_arr = []

    next_index = k-1                           # next index = 2
    people_arr = list(range(1, n+1))            #people_arr =

    while people_arr:                               #
        result = people_arr.pop(next_index)                # result 첫번째 people_arr[2] 삭제
        result_arr.append(result)                           # result에 3추가

        if len(people_arr) != 0:                                        #people_arr가 비어있는지 판별
            next_index = (next_index + (k-1)) % len(people_arr)          # next = (2+2) % 6
            print(next_index)
    print("<", ", " .join(map(str, result_arr)), ">", sep='')


n, k = map(int, input().split())
josephus_problem(n, k)
