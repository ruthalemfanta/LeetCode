def puzzles():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    mini = float('inf')
    for i in range(m - n + 1):
        mini = min(arr[i + n - 1] - arr[i], mini)

    print(mini)

if __name__ == "__main__":
    puzzles()
