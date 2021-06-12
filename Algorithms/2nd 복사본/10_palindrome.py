def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])



    # n = len(string)
    # for i in range(n):
    #     if string[i] != string[n - 1 - i]:
    #         return False
    #
    # return True

input = "토마토마"
print(is_palindrome(input))
