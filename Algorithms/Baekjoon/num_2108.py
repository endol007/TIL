from collections import Counter
import sys
T = int(sys.stdin.readline())
numbers = []

for i in range(T):
    num = int(sys.stdin.readline())
    numbers.append(num)


def first_answer(a):
    return round(sum(a) / len(a))


def second_answer(a):
    a.sort()
    return a[len(a)//2]


def third_answer(a):
    fre_dict = Counter(a)
    fre = fre_dict.most_common()

    if len(a) > 1:
        if fre[0][1] == fre[1][1]:
            answer = fre[1][0]
        else:
            answer = fre[0][0]
    else:
        answer = fre[0][0]
    return answer


def forth_answer(a):
    return max(a) - min(a)


print(first_answer(numbers))
print(second_answer(numbers))
print(third_answer(numbers))
print(forth_answer(numbers))


