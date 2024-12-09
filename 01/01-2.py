with open("prompt-01.txt", "r") as file:
    a = []
    b = []

    for line in file.readlines():
        c = line.strip().split("   ")
        a.append(int(c[0]))
        b.append(int(c[1]))

    c = {}

    for e in b:
        if e in c:
            print(c[e])
            c[e] += 1
        else:
            c[e] = 1

    total = sum([i * (c[i] if i in c else 0) for i in a])

    print(total)
