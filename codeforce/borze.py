def borze(s):
    num = ""
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '.':
            num += '0'
            i += 1
        elif s[i] == '-' and i + 1 < n and s[i + 1] == '.':
            num += '1'
            i += 2
        else:
            num += '2'
            i += 2

    return num

if __name__ == "__main__":
    s = input()
    print(borze(s))