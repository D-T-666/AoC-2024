import matplotlib.pyplot as plt
import matplotlib.animation as animation

w,h = 101, 103
with open("prompt.txt", "r") as file:
  robots = [
    [[int(x) for x in e[2:].split(",")] for e in line.split()] for line in file.read().strip().split("\n")
  ]

  fig = plt.figure()

  im = plt.imshow([[1 if i == j else 0 for j in range(w)] for i in range(h)], animated=True)

  fc = 0
  def update(*args):
    global robots, fc
    valid = False
    final_map = []
    while not valid:
      map = [[0 for j in range(w)] for i in range(h)]
      for r in robots:
        x = r[0][0] = (r[0][0] + r[1][0]) % w
        y = r[0][1] = (r[0][1] + r[1][1]) % h
        map[y][x] = 1
      fc += 1

      for i in range(h - 3):
        for j in range(w - 3):
          if map[i][j] and map[i][j + 1] and map[i][j + 2] and \
              map[i + 1][j] and map[i + 1][j + 1] and map[i + 1][j + 1] and \
              map[i + 2][j] and map[i + 2][j + 1] and map[i + 2][j + 2]:
            valid = True
            break
      final_map = map
    print(fc)
    for line in final_map:
      print("".join("#" if x > 0 else "." for x in line))

    im.set_array(final_map)
    return im,

  ani = animation.FuncAnimation(fig, update, interval=50, blit=True)
  plt.show()
