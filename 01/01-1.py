with open("prompt-01.txt", "r") as file:
    a = []
    b = []

    for line in file.readlines():
        c = line.strip().split("   ")
        a.append(int(c[0]))
        b.append(int(c[1]))

    a.sort()
    b.sort()

    total = sum([abs(i - j) for i, j in zip(a, b)])

    print(total)
