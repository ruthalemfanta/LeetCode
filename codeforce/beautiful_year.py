def beautiful_year():
    year = int(input())

    while True:
        year += 1
        syear = str(year)

        set_year = set(syear)

        if len(set_year) == 4:
            print(year)
            break


if __name__ == "__main__":
    beautiful_year()