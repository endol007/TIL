input = "01010100010"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_zero = 0
    count_one = 0
    if string[0] == '0':
        count_one += 1
    elif string[0] == '1':
        count_zero += 1
    for i in range(len(string) -1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                count_one += 1
            if string[i+1] == '1':
                count_zero += 1
    return min(count_zero, count_one)
    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)