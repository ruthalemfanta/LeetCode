def young():
    n = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(n)]

    x = sum(arr[i][0] for i in range(n))
    y = sum(arr[i][1] for i in range(n))
    z = sum(arr[i][2] for i in range(n))

    if x == y == z == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    young()


    