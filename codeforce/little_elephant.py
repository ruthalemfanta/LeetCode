def littleElephant(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [2, 1]
    else:
        p = [n] + list(range(1, n))
        return p

if __name__ == "__main__":
    n = int(input())
    result = littleElephant(n)
    print(" ".join(map(str, result)))