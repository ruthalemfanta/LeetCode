def cupboards():
    n = int(input())
    l = []
    r = []

    for i in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)

    l_one = 0
    l_zero = 0
    r_one = 0
    r_zero = 0

    for i in range(n):
        if l[i] == 0:
            l_zero += 1
            if r[i] == 0:
                r_zero += 1
            elif r[i] == 1:
                r_one += 1
        else:
            l_one += 1
            if r[i] == 0:
                r_zero += 1
            elif r[i] == 1:
                r_one += 1

    ans = 0
    if l_zero > l_one:
        ans += l_one
    else:
        ans += l_zero

    if r_zero > r_one:
        ans += r_one
    else:
        ans += r_zero

    print(ans)


if __name__ == "__main__":
    cupboards()