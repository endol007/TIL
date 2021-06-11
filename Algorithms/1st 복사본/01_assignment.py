def find_prime_list_under_number(number):
    number_list = []

    for num in range(2, number+1):
        for a in number_list:
            if num % a == 0 and a * a <= num:
                break
        else:
            number_list.append(num)

    return number_list


input = 20
result = find_prime_list_under_number(input)
print(result)