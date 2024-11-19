def HQ9Plus():
    s = input()
    flag = False
    for c in s:
        if c == 'H' or c == 'Q' or c == '9':
            flag = True
            break

    if flag:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    HQ9Plus()
    