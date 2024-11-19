def reconnaissence():
    n = int(input())
    arr = list(map(int, input().split()))

    min_diff = float('inf')
    first = 0

    for i in range(n - 1):
        if min_diff > abs(arr[i] - arr[i + 1]):
            min_diff = abs(arr[i] - arr[i + 1])
            first = i

    if min_diff > abs(arr[0] - arr[n - 1]):
        print(n, 1)
    else:
        print(first + 1, first + 2)

if __name__ == "__main__":
    reconnaissence()
