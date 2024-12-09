import re


with open("prompt-03.txt", "r") as file:
    res = 0

    all_muls = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", file.read())
    for mul in all_muls:
        z = mul[4:-1].split(',')
        res += int(z[0]) * int(z[1])

    print(res)
