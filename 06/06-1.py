with open("prompt-06.txt", "r") as file:
  dirs = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
  ]

  omap = [list(line.strip()) for line in file.read().strip().split()]
  pos = (0, 0)
  dir = 0
  for i in range(len(omap)):
    for j in range(len(omap[i])):
      if omap[i][j] == "^":
        pos = (i, j)
  map = [[omap[i][j] if (i, j) != pos else "." for j in range(len(omap[i]))] for i in range(len(omap))]

  while True:
    npos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
    if not (0 < pos[0] < len(omap) - 1 and 0 < pos[1] < len(omap[0]) - 1):
      break
    if map[npos[0]][npos[1]] != "#":
      map[npos[0]][npos[1]] = "X"
      pos = npos
    else:
      dir = (dir + 1) % 4

  total = 0
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] == "X":
        total += 1
  print(total)
