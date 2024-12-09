from rich import print

pattern = "XMAS"

def rotate(mat):
  return [
    [
      mat[i][j] for i in range(len(mat))[::-1]
    ] for j in range(len(mat[0]))
  ]

def diagonalize(mat):
  return [
    [
      mat[i][j - i] if 0 <= j - i < len(mat[0]) else ' '
      for j in range(len(mat[0]) + len(mat) - 1)
    ] for i in range(len(mat))
  ]

def count(mat):
  print("\n".join(["".join(line) for line in mat]))
  total = 0

  for i in range(len(mat)):
    at = 0
    for j in range(len(mat[i])):
      if mat[i][j] == pattern[at]:
        at += 1
        if at + 1 == 5:
          total += 1
          at = 0
      else:
        at = 0
    if at + 1 == 5:
      total += 1

  print(total)
  return total

with open("prompt-04.txt", "r") as file:
  text = file.read();

  matrix = [list(line.strip()) for line in text.strip().split("\n")];
  # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

  total = 0

  total += count(matrix)
  total += count(rotate(matrix))
  total += count(rotate(rotate(matrix)))
  total += count(rotate(rotate(rotate(matrix))))

  total += count(rotate(diagonalize(matrix)))
  total += count(rotate(rotate(rotate(diagonalize(matrix)))))
  total += count(rotate(diagonalize(rotate(matrix))))
  total += count(rotate(rotate(rotate(diagonalize(rotate(matrix))))))

  print(total)
