n = input().upper()
t = []

for i in set(n):
    t.append(n.count(i))
idx = [i for i,x in enumerate(t) if x == max(t)]
if len(idx) > 1:
    print("?")
else:
    print(list(set(n))[t.index(max(t))])