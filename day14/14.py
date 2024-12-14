import re
import sys  # noqa: F401


filename = "day14/input.txt"


robots = []

# TEST VALUES
# W = 11
# H = 7

W = 101
H = 103

for line in open(filename):
    robots.append(tuple(map(int, re.findall(r'-?\d+', line))))


# PART 1
# for px, py, vx, vy in robots:
#     x_mod = (px + vx * 100) % W
#     y_mod = (py + vy * 100) % H
#     output.append((x_mod, y_mod))


# PART 2
# min_area = float('inf')
min_safety_factor = float('inf')
min_time = None

for step in range(W * H):
    output = []
    q1 = q2 = q3 = q4 = 0
    for px, py, vx, vy in robots:
        x_mod = (px + vx * step) % W
        y_mod = (py + vy * step) % H
        output.append((x_mod, y_mod))

    # xs = [p[0] for p in output]
    # ys = [p[1] for p in output]

    # width = max(xs) - min(xs) + 1
    # height = max(ys) - min(ys) + 1

    # area = width * height

    # if area < min_area:
    #     min_area = area
    #     min_time = step

    for px, py in output:
        if px < (W - 1)//2 and py < (H - 1)//2:
            q1 += 1
        elif px > (W - 1)//2 and py < (H - 1)//2:
            q2 += 1
        elif px < (W - 1)//2 and py > (H - 1)//2:
            q3 += 1
        elif px > (W - 1)//2 and  py > (H - 1)//2:
            q4 += 1

    safety_factor = q1 * q2 * q3 * q4

    if safety_factor < min_safety_factor:
        min_safety_factor = safety_factor
        min_time = step

print(min_safety_factor, min_time)