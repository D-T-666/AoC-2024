def rotate(mat):
  return [
    [
      mat[i][j] for i in range(len(mat))[::-1]
    ] for j in range(len(mat[0]))
  ]

def count(mat):
  total = 0

  for i in range(1, len(mat) - 1):
    for j in range(1, len(mat[i]) - 1):
      valid = mat[i][j] == 'A'
      valid &= mat[i-1][j-1] == 'M'
      valid &= mat[i+1][j+1] == 'S'
      valid &= mat[i-1][j+1] == 'M'
      valid &= mat[i+1][j-1] == 'S'
      if valid:
        total += 1

  return total

with open("prompt-04.txt", "r") as file:
  text = file.read();

  matrix = [list(line.strip()) for line in text.strip().split("\n")];

  total = 0

  total += count(matrix)
  total += count(rotate(matrix))
  total += count(rotate(rotate(matrix)))
  total += count(rotate(rotate(rotate(matrix))))

  print(total)
