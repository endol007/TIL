a = int(input())
a_list = list()
for _ in range(a):
    count = 0
    arr = list(map(int, input().split()))
    avg = (sum(arr)-arr[0])/arr[0]
    for i in arr[1:]:
        if i > avg:
            count+=1
    r = count/arr[0]*100
    a_list.append(r)
for t in range(len(a_list)):
    print(f"{a_list[t]:.3f}%", sep="\n")