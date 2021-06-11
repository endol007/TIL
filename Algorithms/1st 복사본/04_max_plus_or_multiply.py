def find_max_plus_or_multiply(array):
    multi = 0;
    for num in array:
        if num <= 1 or multi <= 1:
            multi += num
        else:
            multi *= num
    return multi


result = find_max_plus_or_multiply
print("", result([0,3,5,6,1,2,4]))