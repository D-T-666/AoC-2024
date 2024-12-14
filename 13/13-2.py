with open("prompt-13.txt", "r") as file:
  machines = [[[int(x[2:]) for x in e.split(": ")[1].split(", ")] for e in m.strip().split("\n")] for m in file.read().strip().split("\n\n")]

  total = 0
  for m in machines:
    m[2][0] += 10000000000000
    m[2][1] += 10000000000000
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]

    a = m[1][1] * m[2][0] - m[1][0] * m[2][1]
    b = -m[0][1] * m[2][0] + m[0][0] * m[2][1]

    if a % det == 0 and b % det == 0:
      total += (3 * a + b) // det

  print(total)
