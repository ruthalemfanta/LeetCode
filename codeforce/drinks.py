def drinks():
    n = int(input())
    sum = 0.0
    numbers = input().split()
    for i in range(n):
        temp = float(numbers[i])
        sum += temp
    print(f"{sum/n:.15f}")

if __name__ == "__main__":
    drinks()