import sys
N = int(sys.stdin.readline())

people = list(map(int, sys.stdin.readline().split()))
people.sort()
time_list = []
cnt = 0
while True:
    if cnt == 0:
        time_list.append(people[0])
        cnt += 1
    else:
        time_list.append(people[cnt] + time_list[cnt-1])
        cnt += 1

    if cnt == N:
        break
print(sum(time_list))