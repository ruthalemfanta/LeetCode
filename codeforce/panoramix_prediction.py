def check_prime(x):
    if x == 2 or x == 3:
        return True

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def panoramixPrediction():
    n, m = map(int, input().split())

    if not check_prime(m):
        print("NO")
    else:
        for i in range(n + 1, m + 1):
            if check_prime(i):
                if i == m:
                    print("YES")
                else:
                    print("NO")
                break

if __name__ == "__main__":
    panoramixPrediction()
    