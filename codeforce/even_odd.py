def evenOdd():
    n, k = map(int, input().split())
    n_odds = n - n // 2
    if k <= n_odds:
        print(1 + (k - 1) * 2)
    else:
        print(2 + (k - n_odds - 1) * 2)

if __name__ == "__main__":
    evenOdd()
