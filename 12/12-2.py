from rich import print

# with open("test.txt", "r") as file:
with open("prompt-12.txt", "r") as file:
  mat = [list(line.strip()) + [None] for line in file.read().strip().split()]
  mat += [[None for i in range(len(mat[0]))]]

  total = 0

  visited = [
    [False for i in range(len(mat[j]))]
    for j in range(len(mat))
  ]

  for ii in range(len(mat) - 1):
    for jj in range(len(mat[ii]) - 1):
      if not visited[ii][jj]:
        c = mat[ii][jj]
        stack = [(ii, jj)]
        cells = set()

        while len(stack) > 0:
          i, j = stack.pop()
          if visited[i][j]: continue

          cells.add((i, j))

          neighbors = 0
          if i < len(mat) - 1 and mat[i + 1][j] == c:
            if not visited[i + 1][j]: stack.append((i + 1, j))
            neighbors += 1 if visited[i + 1][j] else 0
          if i > 0 and mat[i - 1][j] == c:
            if not visited[i - 1][j]: stack.append((i - 1, j))
            neighbors += 1 if visited[i - 1][j] else 0
          if j < len(mat[0]) - 1 and mat[i][j + 1] == c:
            if not visited[i][j + 1]: stack.append((i, j + 1))
            neighbors += 1 if visited[i][j + 1] else 0
          if j > 0 and mat[i][j - 1] == c:
            if not visited[i][j - 1]: stack.append((i, j - 1))
            neighbors += 1 if visited[i][j - 1] else 0

          visited[i][j] = True

        edges = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        # 01 - right
        # 10 - down
        for (i, j) in cells:
          if (i - 1, j) not in cells:
            edges[i][j] |= 1
          if (i, j - 1) not in cells:
            edges[i][j] |= 2
          if (i + 1, j) not in cells:
            edges[i + 1][j] |= 1
          if (i, j + 1) not in cells:
            edges[i][j + 1] |= 2

        sides = 0
        for i in range(len(mat)):
          for j in range(len(mat[0])):
            if edges[i][j] & 1 != 0:
              sides += 1
              for k in range(j + 1, len(mat[0])):
                if edges[i][k] & 1 == 0:
                  break
                if mat[i][j] == c:
                  if mat[i][k] != c:
                    break
                if mat[i - 1][j] == c:
                  if mat[i - 1][k] != c:
                    break
                edges[i][k] ^= 1
            if edges[i][j] & 2 != 0:
              sides += 1
              for k in range(i + 1, len(mat)):
                if edges[k][j] & 2 == 0:
                  break
                if mat[i][j] == c:
                  if mat[k][j] != c:
                    break
                if mat[i][j - 1] == c:
                  if mat[k][j - 1] != c:
                    break
                edges[k][j] ^= 2

        total += len(cells) * sides

  print(total)
