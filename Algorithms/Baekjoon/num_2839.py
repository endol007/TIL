# 첫번쨰 풀이
# sugar_kg = int(input())
# def sanggn(num):
#     a = int(num//3)
#     b = int(num//5)
#     sugar_list = []
#     for i in range(a+1):
#         for j in range(b+1):
#             if i * 3 + j * 5 == num:
#                 sugar_list.append(i+j)
#     sugar_list.sort()
#     if len(sugar_list) == 0:
#         return -1
#     else:
#         return sugar_list[0]
#
#
# print(sanggn(sugar_kg))

sugar_kg = int(input())

bag = 0
while sugar_kg >= 0 :
    if sugar_kg % 5 == 0 :
        bag += (sugar_kg // 5)
        print(bag)
        break
    sugar_kg -= 3
    bag += 1
else :
    print(-1)