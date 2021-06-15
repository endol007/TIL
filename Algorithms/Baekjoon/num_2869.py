a, b, v = map(int, input().split())
m = 0
if (v-b) % (a-b) !=0:
    m = ((v-b)//(a-b)) + 1
else:
    m = ((v-b)//(a-b))
print(m)



(v - b) % (a - b) 