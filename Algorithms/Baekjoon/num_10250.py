test_case = int(input())
room = []
for i in range(test_case):
    h, w, people = map(int, input().split())
    f = 0
    ho = 0
    if people % h == 0:
        f = h * 100
        ho = people // h
    else:
        f = (people % h) * 100
        ho = 1 + people // h
    print(f + ho)
