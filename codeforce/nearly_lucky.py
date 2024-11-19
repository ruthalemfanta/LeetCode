def nearlyLucky():
    n = int(input())
    c = 0

    while n:
        x = n % 10
        if x == 4 or x == 7:
            c += 1
        n = n // 10

    if c == 4 or c == 7:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    nearlyLucky()
