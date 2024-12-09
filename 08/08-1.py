from rich import print

def check_bounds(p, bounds):
  if p[0] < 0 or p[1] < 0:
    return False
  if p[0] >= bounds[0] or p[1] >= bounds[1]:
    return False
  return True

with open("prompt-08.txt", "r") as file:
# with open("test.txt", "r") as file:
  grid = [list(line.strip()) for line in file.read().strip().split()]

  h, w = len(grid), len(grid[0])

  chars = set()
  for row in grid:
    for el in row:
      chars |= {el}
  chars -= {"."}

  total = 0

  antinodes = set()
  for char in chars:
    positions = set()
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == char:
          positions |= {(i, j)}

    for a in positions:
      for b in positions:
        if a == b: continue

        p = (2 * a[0] - b[0], 2 * a[1] - b[1])
        q = (2 * b[0] - a[0], 2 * b[1] - a[1])

        if p not in antinodes:
          if check_bounds(p, (h, w)):
            antinodes |= {p}

        if q not in antinodes:
          if check_bounds(q, (h, w)):
            antinodes |= {q}


  total = len(antinodes)
  print(antinodes)

  print(total)

  # print(chars)
