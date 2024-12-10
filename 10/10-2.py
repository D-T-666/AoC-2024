def score(map: list[list[int]], i: int, j: int) -> int:
  if map[i][j] == 9:
    return 1
  v = map[i][j] + 1
  res = 0
  if i + 1 < len(map) and map[i + 1][j] == v:
    res += score(map, i + 1, j)
  if i - 1 >= 0 and map[i - 1][j] == v:
    res += score(map, i - 1, j)
  if j + 1 < len(map[i]) and map[i][j + 1] == v:
    res += score(map, i, j + 1)
  if j - 1 >= 0 and map[i][j - 1] == v:
    res += score(map, i, j - 1)
  return res

with open("prompt-10.txt", "r") as file:
  map = [
    [int(x) for x in line.strip()]
    for line in file.read().strip().split()
  ]

  total = 0
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] != 0: continue
      total += score(map, i, j)

  print(total)
