from rich import print

# with open("test.txt", "r") as file:
with open("prompt-12.txt", "r") as file:
  mat = [list(line.strip()) for line in file.read().strip().split()]

  total = 0

  visited = [
    [False for i in range(len(mat[j]))]
    for j in range(len(mat))
  ]

  for ii in range(len(mat)):
    for jj in range(len(mat[ii])):
      if not visited[ii][jj]:
        c = mat[ii][jj]
        stack = [(ii, jj)]

        area = 1
        peri = 4

        while len(stack) > 0:
          i, j = stack.pop()
          if visited[i][j]: continue


          neighbors = 0
          if i < len(mat) - 1 and mat[i + 1][j] == c:
            if not visited[i + 1][j]:
              stack.append((i + 1, j))
            neighbors += 1 if visited[i + 1][j] else 0
          if i > 0 and mat[i - 1][j] == c:
            if not visited[i - 1][j]:
              stack.append((i - 1, j))
            neighbors += 1 if visited[i - 1][j] else 0
          if j < len(mat[0]) - 1 and mat[i][j + 1] == c:
            if not visited[i][j + 1]:
              stack.append((i, j + 1))
            neighbors += 1 if visited[i][j + 1] else 0
          if j > 0 and mat[i][j - 1] == c:
            if not visited[i][j - 1]:
              stack.append((i, j - 1))
            neighbors += 1 if visited[i][j - 1] else 0

          if i == ii and j == jj:
            area = 1
            peri = 4
            visited[ii][jj] = True
          else:
            area += 1
            peri += 4 - neighbors * 2

          visited[i][j] = True

        total += area * peri

  print(total)

  # print("\n".join(["".join([str(x) for x in line]) for line in inds]))

  # print(peri)
  # print(area)
  # print("\n".join([f'{p} * {a}' for p, a in zip(peri, area)]))
  # print(sum([p * a for p, a in zip(peri, area)]))
