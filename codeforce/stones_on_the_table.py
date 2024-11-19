def stones(n, s):
    ans = 0
    l = len(s)
    last = s[0]

    for i in range(1, l):
        if last == s[i]:
            ans += 1
        last = s[i]

    return ans

n = int(input().strip())
s = input().strip()
print(stones(n, s))
