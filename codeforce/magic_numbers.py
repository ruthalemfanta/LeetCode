def magicNumbers():
    n = input().strip()  
    flag = False
    cnt = 0

    if n[0] == '1':
        for i in range(len(n)):
            if n[i] == '1' or n[i] == '4':
                cnt += 1
                if n[i] == '4':
                    if cnt > 3 and n[i-1] == '4' and n[i-2] == '4':
                        flag = True
                        break
            else:
                flag = True
                break
    else:
        flag = True

    if flag:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    magicNumbers()
