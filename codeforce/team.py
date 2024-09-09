def team():
    n = int(input())
    q = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        if a + b + c >= 2:
            q += 1
    print(q)

team()
