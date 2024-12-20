import re
from egcd import egcd

filename = "day13/input.txt"

def read_input():

    machines = []
    with open(filename, mode='r') as file:
        data = file.readlines()

        machine = {}

        for line in data:
            line = line.strip()

            if line.startswith("Button A:"):
                parts = line.split(", ")
                ax = int(parts[0].split("+")[1])
                ay = int(parts[1].split("+")[1])
                machine['A'] = (ax, ay)
            elif line.startswith("Button B:"):
                parts = line.split(", ")
                bx = int(parts[0].split("+")[1])
                by = int(parts[1].split("+")[1])
                machine['B'] = (bx, by)
            elif line.startswith("Prize:"):
                parts = line.split(", ")
                px = int(parts[0].split("=")[1])
                py = int(parts[1].split("=")[1])
                machine['Prize'] = (px, py)
            elif line == '':
                machines.append(machine)
                machine = {}

        if machine:
            machines.append(machine)
    return machines


def find_min_cost(prize, ba, bb, max_presses=100):
    px, py = prize
    ax, ay = ba
    bx, by = bb

    def solve_axis(target, da, db):
        g, x0, y0 = egcd(da, db)
        if target % g != 0:
            return None, None, None
        
        x0 *= target // g
        y0 *= target // g
        return x0, y0, g
    
    x0, y0, gx = solve_axis(px, ax, bx)
    z0, w0, gy = solve_axis(py, ay, by)
    
    # print(gx, gy)
    best_cost = float('inf')

    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            if a * ax + b * bx == px and a * ay + b * by == py:
                cost = 3 * a + b
                best_cost = min(best_cost, cost)

    return best_cost if best_cost != float('inf') else None


def solve_(machines):
    total_cost = 0
    total_prize = 0

    for machine in machines:
        ba = machine['A']
        bb = machine['B']
        prize = machine['Prize']

        # print(prize)
        cost = find_min_cost(prize, ba, bb)
        # print(ba, bb, prize, cost)

        if cost is not None:
            total_cost += cost
            total_prize += 1
    
    return total_prize, total_cost


# machines = read_input_using_regex()
# print(machines)
# offset = 10**13
# for machine in machines:
#     px, py = machine['Prize']
#     machine['Prize'] = (px + offset, py + offset)

# total_prize, total_cost = solve_(machines)
# print(total_prize, total_cost)


total_cost = 0
for data in open(filename).read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r'\d+', data))

    px += 10000000000000
    py += 10000000000000

    # print(ax, ay, bx, by, px, py)
    b_a = (px * by - py * bx) / (ax * by - ay * bx)
    b_b = (px - b_a * ax) / bx

    # print(b_a, b_b)
    if b_a % 1 == b_b % 1 == 0:
        total_cost += int(3 * b_a + b_b)

print(total_cost)