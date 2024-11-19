def numberOfPos(n, a, b):
    cnt = 0
    for i in range(n):
        if n - (i + 1) <= b and i + 1 > a:
            cnt += 1
    return cnt

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    print(numberOfPos(n, a, b))

    