def is_number_exist(array):
    number = 3
    for element in array:
        if number == element:
            return number
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result([4,5,6,1,2,4]))