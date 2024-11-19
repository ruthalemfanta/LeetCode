def translation():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)

    if s_len != t_len:
        print("NO")
    else:
        flag = True
        for i in range(s_len):
            if s[i] != t[s_len - i - 1]:
                flag = False
                break

        if flag:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    translation()
    