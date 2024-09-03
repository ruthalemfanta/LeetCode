def wayTooLongWords(n, w):
    for i in w:
        if len(i) > 10:
            print(i[0] + str(len(i) - 2) + i[-1])
        else:
            print(i)

n = int(input())
w = []
for i in range(n):
    w.append(input())
wayTooLongWords(n, w)