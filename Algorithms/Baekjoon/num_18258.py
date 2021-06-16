import sys
from collections import deque

T = int(sys.stdin.readline())
queue = deque([])
for i in range(T):
    order = sys.stdin.readline().split()
    if 'push' in order:
        queue.append(order[1])
    elif 'front' in order:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in order:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif 'size' in order:
        print(len(queue))
    elif 'empty' in order:
        if len(queue) == 0:
            print(1)
        elif len(queue) > 0:
            print(0)
    elif 'pop' in order:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

#큐삭제할때 그냥 pop함수를 쓰면 전체 값들이 앞으로 한칸씩 땡겨지는데에 시간이 걸리므로 popleft함수를 이용해서 pop을 구현
