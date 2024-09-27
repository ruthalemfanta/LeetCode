def petya():
    s, t = input(), input()
    if s.lower() < t.lower():
        print(-1)
    elif s.lower() > t.lower():
        print(1)
    else:
        print(0)


petya()