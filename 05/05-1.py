with open("prompt-05.txt", "r") as file:
  text = file.read();
  total = 0

  relation = set()
  sections = text.split("\n\n")
  for line in sections[0].strip().split():
    relation.add(line.strip())

  for line in sections[1].strip().split():
    arr = line.strip().split(",")

    valid = True

    for i in range(len(arr)):
      for j in range(i+1, len(arr)):
        valid &= not (str(arr[j]) + "|" + str(arr[i]) in relation)

    if valid:
      total += int(arr[len(arr) // 2])

  print(total)
