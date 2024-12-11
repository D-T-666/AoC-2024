def magic(x, d):
  if d == 0:
    return 1

  if (l := len(str(x))) % 2 == 0:
    return magic(int(str(x)[:l//2]), d - 1) + magic(int(str(x)[l//2:]), d - 1)
  elif x != 0:
    return magic(x * 2024, d - 1)
  else:
    return magic(1, d - 1)

with open("prompt-11.txt", "r") as file:
  res = sum([magic(int(x), 25) for x in file.read().strip().split()])
  print(res)
