with open("prompt-02.txt", "r") as file:
    data = []
    for line in file.readlines():
        data.append([int(x) for x in line.strip().split()])

    total = 0
    for reading in data:
        ot = False
        for j in range(len(reading)):
            perm = reading[:j] + reading[j+1:]

            inc = True
            dec = True
            for i in range(len(perm) - 1):
                c = perm[i + 1] - perm[i]
                if c < 1 or c > 3:
                    inc = False
                if c > -1 or c < -3:
                    dec = False
            ot |= inc or dec
        if ot:
            total += 1
    print(total)
