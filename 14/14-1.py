w,h = 101, 103
with open("prompt.txt", "r") as file:
  robots = [
    [[int(x) for x in e[2:].split(",")] for e in line.split()] for line in file.read().strip().split("\n")
  ]

  quads = [0,0,0,0]

  for r in robots:
    x = (r[0][0] + r[1][0] * 100) % w
    y = (r[0][1] + r[1][1] * 100) % h

    ind = -1
    if x != w // 2 and y != h // 2:
      ind = (1 if y < h // 2 else 0) * 2 + (1 if x < w // 2 else 0)

    if ind > -1:
      quads[ind] += 1

  print(quads[0] * quads[1] * quads[2] * quads[3])
