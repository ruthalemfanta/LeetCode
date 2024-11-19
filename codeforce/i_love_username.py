def iLoveUsername():
    n = int(input())

    arr = list(map(int, input().split()))

    ans = 0
    max_val = arr[0]
    min_val = arr[0]
    for i in range(1, n):
        if max_val < arr[i]:
            max_val = arr[i]
            ans += 1

        if min_val > arr[i]:
            min_val = arr[i]
            ans += 1

    print(ans)


if __name__ == "__main__":
    iLoveUsername()