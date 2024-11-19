def isYourHorse():
    s = set()
    numbers = input().split()
    for i in range(4):
        temp = int(numbers[i])
        s.add(temp)
    print(4 - len(s))

if __name__ == "__main__":
    isYourHorse()