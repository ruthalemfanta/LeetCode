def softDrinks():
    n, k, l, c, d, p, nl, np = map(int, input().split())

    ans = min((k * l) // nl, p // np, c * d) // n
    print(ans)

if __name__ == "__main__":
    softDrinks()

