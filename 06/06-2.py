from rich import print

dirs = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
]

def has_loop(_map, _pos):
  map = _map.copy()
  pos = (_pos[0], _pos[1])
  dir = 0
  while True:
    npos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])

    if not (0 < pos[0] < len(omap) - 1 and 0 < pos[1] < len(omap[0]) - 1):
      return False

    if map[pos[0]][pos[1]] & (1 << dir) != 0:
      return True
    map[pos[0]][pos[1]] |= 1 << dir

    if map[npos[0]][npos[1]] != -1:
      pos = npos
    else:
      dir = (dir + 1) % 4

with open("prompt-06.txt", "r") as file:
# with open("test.txt", "r") as file:

  omap = [list(line.strip()) for line in file.read().strip().split()]
  pos = (0, 0)
  dir = 0
  for i in range(len(omap)):
    for j in range(len(omap[i])):
      if omap[i][j] == "^":
        pos = (i, j)
  asdfasd  = {
    "#": -1,
    ".": 0,
  }
  map = [[asdfasd[omap[i][j]] if (i, j) != pos else 0 for j in range(len(omap[i]))] for i in range(len(omap))]

  total = 0
  for i in range(len(map)):
    for j in range(len(map[i])):
      if (i, j) == pos:
        continue
      o = map[i][j]
      map[i][j] = -1
      if has_loop(map, pos):
        map = [[asdfasd[omap[i][j]] if (i, j) != pos else 0 for j in range(len(omap[i]))] for i in range(len(omap))]
        map[i][j] = -1
        # print("\n".join([" ".join([str(x) for x in e]) for e in map]))
        # print()
        total += 1
      map = [[asdfasd[omap[i][j]] if (i, j) != pos else 0 for j in range(len(omap[i]))] for i in range(len(omap))]
  print(total)
