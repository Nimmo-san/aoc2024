from egcd import egcd


def read_input():
    filename = "day13/input.txt"

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
                cost = 3 * a + 1 * b
                best_cost = min(best_cost, cost)

    return best_cost if best_cost != float('inf') else None


def e_gcd(a, b):
    pass


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


machines = read_input()
total_prize, total_cost = solve_(machines)
print(total_prize, total_cost)