from rich import print

# with open("test.txt", "r") as file:
with open("prompt-09.txt", "r") as file:
  arr = [int(c) for c in file.read().strip()]
  moved = [False for _ in arr]

  arr = [[arr[i], i // 2 if i % 2 == 0 else -1] for i in range(len(arr))]

  for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
      if i % 2 == 1: continue
      if arr[j][1] == -1 and arr[j][0] >= arr[i][0]:
        arr[j][0] -= arr[i][0]
        t = arr[i].copy()
        arr[i][1] = -1
        arr.insert(j, t)
        if arr[j + 1][0] == 0:
          arr.pop(j + 1)

  res = 0
  c = 0
  for e in arr:
    if e[1] == -1:
      c += e[0]
      # print("." * e[0], end="")
    else:
      for _ in range(e[0]):
        res += e[1] * c
        c += 1
      # print(str(e[1]) * e[0], end="")
  # print()

  print(res)

# 00992111777.44.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..
