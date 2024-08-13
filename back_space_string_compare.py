def backSpaceCompare(s, t):
    for i in range(len(s)-1) :
        if s[i] == "#":
            s = s[:i-1] + s[i+1:]

    for j in range(len(t)-1) :
        if t[j] == "#":
            t = t[:j-1] + t[j+1:]
    if s == t:
        return True
    else:
        return False


s = "ab##"
t = "c#d#"


print(backSpaceCompare(s,t))