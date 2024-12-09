with open("prompt-02.txt", "r") as file:
    data = []
    for line in file.readlines():
        data.append([int(x) for x in line.strip().split()])

    total = 0
    for reading in data:
        inc = True
        dec = True
        for i in range(len(reading) - 1):
            c = reading[i + 1] - reading[i]
            if c < 1 or c > 3:
                inc = False
            if c > -1 or c < -3:
                dec = False
        if inc or dec:
            total += 1
    print(total)
