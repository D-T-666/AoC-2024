from rich import print

# with open("test.txt", "r") as file:
with open("prompt-09.txt", "r") as file:
  arr = [int(c) for c in file.read().strip()]

  print(arr)
  res = 0
  c = 0
  r = len(arr) - 1 if len(arr) % 2 == 1 else len(arr) - 2
  l = 0
  s = ""
  while l <= r:
    if arr[l] == 0:
      l += 1
    else:
      if l % 2 == 0:
        arr[l] -= 1
        res += c * (l // 2)
        # s += f" + {c} * {l//2}"
        c += 1
      else:
        # erti cali unda wamovigo bolodan
        if arr[r] == 0:
          r -= 2
        else:
          res += c * (r // 2)
          # s += f" + {c} * {r//2}"
          arr[l] -= 1
          arr[r] -= 1
          c += 1
  # print(s)

  print(res)
