def ultra():
    n = input()
    m = input()

    ans = ""
    for i in range(len(n)):
        if n[i] != m[i]:
            ans += '1'
        else:
            ans += '0'

    print(ans)

if __name__ == "__main__":
    ultra()