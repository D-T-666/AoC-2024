def score(map: list[list[int]], visited: set[tuple[int, int]], i: int, j: int) -> int:
  if map[i][j] == 9 and (i, j) not in visited:
    visited.add((i, j))
    return 1
  v = map[i][j] + 1
  res = 0
  if i + 1 < len(map) and map[i + 1][j] == v:
    res += score(map, visited, i + 1, j)
  if i - 1 >= 0 and map[i - 1][j] == v:
    res += score(map, visited, i - 1, j)
  if j + 1 < len(map[i]) and map[i][j + 1] == v:
    res += score(map, visited, i, j + 1)
  if j - 1 >= 0 and map[i][j - 1] == v:
    res += score(map, visited, i, j - 1)
  return res

with open("prompt-10.txt", "r") as file:
# with open("test.txt", "r") as file:
  map = [
    [int(x) for x in line.strip()]
    for line in file.read().strip().split()
  ]

  total = 0
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] != 0: continue
      visited = set()
      total += score(map, visited, i, j)

  print(total)
