def chatroom(s):
    c = 0
    for i in range(len(s)):
        if s[i] == 'h' and c == 0:
            c += 1
        elif s[i] == 'e' and c == 1:
            c += 1
        elif s[i] == 'l' and c == 2:
            c += 1
        elif s[i] == 'l' and c == 3:
            c += 1
        elif s[i] == 'o' and c == 4:
            c += 1

    if c == 5:
        return "YES"
    else:
        return "NO"
    
if __name__ == "__main__":
    s = input()
    print(chatroom(s))