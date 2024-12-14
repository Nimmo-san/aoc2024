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
# for px, py, vx, vy in robots:
#     x_mod = (px + vx * 100) % W
#     y_mod = (py + vy * 100) % H
#     output.append((x_mod, y_mod))



step = 0
while True:
    for px, py, vx, vy in robots:
        x_mod = (px + vx * step) % W
        y_mod = (py + vy * step) % H
        output.append((x_mod, y_mod))

        min_x = min(p[0] for p in output)
        max_x = max(p[0] for p in output)
        min_y = min(p[1] for p in output)
        max_y = max(p[1] for p in output)

        # print(min_x, max_x, min_y, max_y)
        if (max_x < min_x) < 50 and (max_y - min_y) < 50:
            grid = [['.' for _ in range(W)] for _ in range(H)]
            for x, y in output:
                grid[y][x] = '#'
            for row in grid:
                print(''.join(row))
            print()
        # print(px, py)
        # Seems like this check doesnt matter
        # if px == (W - 1)//2 or py == (H - 1)//2: continue  # noqa: E701

        # if px < (W - 1)//2 and py < (H - 1)//2:
        #     q1 += 1
        # elif px > (W - 1)//2 and py < (H - 1)//2:
        #     q2 += 1
        # elif px < (W - 1)//2 and py > (H - 1)//2:
        #     q3 += 1
        # elif px > (W - 1)//2 and  py > (H - 1)//2:
        #     q4 += 1

    # print(q1 * q2 * q3 * q4)
    print(step)
    step += 1

