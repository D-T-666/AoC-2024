from rich import print
import math

def can_eval(sequence: list[int], target: int) -> bool:
  for i in range(int(math.pow(3, len(sequence) - 1))):
    val = sequence[0]
    mask = i
    for j in range(1, len(sequence)):
      if mask % 3 == 0:
        val += sequence[j]
      elif mask % 3 == 1:
        val = int(str(val) + str(sequence[j]))
      else:
        val *= sequence[j]
      mask //= 3

    if val == target:
      return True
  return False

# with open("test.txt", "r") as file:
with open("prompt-07.txt", "r") as file:
  total = 0

  for line in file.readlines():
    parts = line.split(":")
    target = int(parts[0].strip())
    sequence = [int(num) for num in parts[1].strip().split()]

    if can_eval(sequence, target):
      total += target

  print(total)
