def beautifulMatrix():
    arrays = [list(map(int, input().split())) for _ in range(5)]

    for i in range(len(arrays)):
        if 1 in arrays[i]:
            row = arrays[i]
            row_i = i
            break

    for j in range(len(row)):
        if row[j] == 1:
            column = j 
                    
    print(abs(column-2) + abs(2 -row_i))

beautifulMatrix()