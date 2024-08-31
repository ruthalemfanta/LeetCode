def minSteps(s,t):
    s = list(s)
    t = list(t)
    for char in s:
        if char in t:
            t.remove(char)
    return len(t)

s = "leetcode"
t = "practice"
print(minSteps(s,t))  