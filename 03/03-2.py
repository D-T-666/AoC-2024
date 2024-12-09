import re


with open("prompt-03.txt", "r") as file:
    res = 0

    all_ops = re.findall(r"(mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\))", file.read())
    enabled = True
    for op in all_ops:
        if op == 'do()':
            enabled = True
        elif op == "don't()":
            enabled = False
        elif enabled:
            z = op[4:-1].split(',')
            res += int(z[0]) * int(z[1])

    print(res)
