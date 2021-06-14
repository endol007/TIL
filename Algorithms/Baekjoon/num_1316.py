import re

num = int(input())
count = 0
for i in range(num):
    s = input()
    s_new = re.sub(r'(.)\1+', r'\1', s)
    string = set(s_new)
    string = list(string)
    if len(s_new) == len(string):
        count +=1
print(count)
