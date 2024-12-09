from rich import print

def can_eval(sequence: list[int], target: int) -> bool:
  # print(sequence)
  for i in range(1 << (len(sequence) - 1)):
    s = "(" * (len(sequence) - 1) + str(sequence[0])
    mask = i
    for j in range(1, len(sequence)):
      if mask % 2 == 0:
        s += " + "
      else:
        s += " * "
      s += str(sequence[j]) + ")"
      mask >>= 1

    if eval(s) == target:
      print(f"{s} = {eval(s)}")
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
