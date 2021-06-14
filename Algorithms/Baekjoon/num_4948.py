# def find_prime_list_under_number(number):
#     number_list = []
#     k= number*2
#     for num in range(2, k+1):
#         for a in number_list:
#             if num % a == 0 and a * a <= num:
#                 break
#         else:
#             number_list.append(num)
#
#     return number_list
#
#
# input = int(input())
# result = find_prime_list_under_number(input)
# new_result = []
# for i in range(len(result)):
#     if result[i] > input:
#         new_result.append(result[i])
#
# print(len(new_result))


def prime_list(n):

    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]

while 1:
    n = int(input())
    if n==0:
        break
    li=prime_list(2*n+1)
    print(len([i for i in li if i>n]))

