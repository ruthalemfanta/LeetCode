def bicycleChain():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    cnt = 0
    maxi = float('-inf')

    for i in range(m):
        for j in range(n):
            if arr2[i] % arr[j] == 0:
                if maxi == arr2[i] // arr[j]:
                    cnt += 1
                elif maxi < arr2[i] // arr[j]:
                    cnt = 1
                    maxi = arr2[i] // arr[j]

    print(cnt)

if __name__ == "__main__":
    bicycleChain()
