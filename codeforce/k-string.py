def kString():
    k = int(input())
    s = input()
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    flag = True
    ans = ""

    for char, count in char_count.items():
        if count % k != 0:
            flag = False
            break
        else:
            ans += char * (count // k)

    if flag:
        print(ans * k)
    else:
        print(-1)

if __name__ == "__main__":
    kString()
