def dragon():
    s, n = map(int, input().split())
    dragons = []

    for _ in range(n):
        temp_d, temp_y = map(int, input().split())
        dragons.append((temp_d, temp_y))

    dragons.sort(key=lambda x: x[0])

    flag = True
    for d, y in dragons:
        if s <= d:
            flag = False
            break
        s += y

    if flag:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    dragon()
