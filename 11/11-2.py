memo = {}

def magic(x, d):
  if d == 0:
    return 1

  if d in memo:
    if x in memo[d]:
      return memo[d][x]

  res = 0
  if (l := len(str(x))) % 2 == 0:
    res = \
      magic(int(str(x)[:l//2]), d - 1) + \
      magic(int(str(x)[l//2:]), d - 1)
  elif x != 0:
    res = magic(x * 2024, d - 1)
  else:
    res = magic(1, d - 1)

  if d not in memo: memo[d] = {}
  memo[d][x] = res

  return res


with open("prompt-11.txt", "r") as file:
  res = sum([magic(int(x), 75) for x in file.read().strip().split()])
  print(res)
