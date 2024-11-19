def amusingJokes():
    try:
        s1, s2, s3 = input().split()
    except ValueError:
        print("Invalid input. Please provide three strings separated by spaces.")
        return

    combined = sorted(s1 + s2)
    target = sorted(s3)

    if combined == target:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    amusingJokes()