import re
import sys


filename = "day14/input.txt"


robots = []

# TEST VALUES
# W = 11
# H = 7

W = 101
H = 103

for line in open(filename):
    robots.append(tuple(map(int, re.findall(r'-?\d+', line))))


output = []
q1 = q2 = q3 = q4 = 0
for px, py, vx, vy in robots:
    x_mod = (px + vx * 100) % W
    y_mod = (py + vy * 100) % H
    output.append((x_mod, y_mod))

for px, py in output:
    # print(px, py)
    # Seems like this check doesnt matter
    # if px == (W - 1)//2 or py == (H - 1)//2: continue  # noqa: E701

    if px < (W - 1)//2 and py < (H - 1)//2:
        q1 += 1
    elif px > (W - 1)//2 and py < (H - 1)//2:
        q2 += 1
    elif px < (W - 1)//2 and py > (H - 1)//2:
        q3 += 1
    elif px > (W - 1)//2 and  py > (H - 1)//2:
        q4 += 1

print(q1 * q2 * q3 * q4)

