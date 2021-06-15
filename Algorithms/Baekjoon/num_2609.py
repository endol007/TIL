num1, num2 = map(int, input().split())
tmp = 0
a = num1
b = num2
while True:
    tmp = b
    b = a % b
    a = tmp
    if b== 0:
        break

print(tmp)
print(int((num1*num2)/tmp))

# if b == 0:
#     break
# elif b > a:
#     tmp = a
# a = b % a
# b = tmp
# if a == 0:
#     break