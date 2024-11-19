def xeniaAndRingroad():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    t = arr[0] - 1

    for i in range(1, m):
        if arr[i] > arr[i - 1]:
            t += arr[i] - arr[i - 1]
        elif arr[i] < arr[i - 1]:
            t += n - arr[i - 1] + arr[i]

    print(t)

if __name__ == "__main__":
    xeniaAndRingroad()
