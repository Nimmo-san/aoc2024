from pprint import pprint  # noqa: F401
from collections import deque  # noqa: F401

filename = "day12/input.txt"

with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]


def calculate_total_price_(grid):
    rows = len(grid)
    cols = len(grid[0])

    visited = set()

    def dfs(x, y, plant_type):
        stack = [(x, y)]
        area = 0
        perimeter = 0

        while stack:
            cx, cy = stack.pop()
            if (cx ,cy) in visited:
                continue

            visited.add((cx, cy))
            area += 1

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == plant_type and (nx, ny) not in visited:
                        stack.append((nx, ny))
                    elif grid[nx][ny] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1
        return area, perimeter
    
    total_price = 0
    for row in range(rows):
        for col in range(cols):
            # print("visiting", row, col)
            if (row, col) not in visited:
                area, perimeter = dfs(row, col, grid[row][col])
                total_price += area * perimeter
                # print(f"total price for ({row},{col}) - {total_price}" )
            # print(total_price)
    return total_price

print(calculate_total_price_(grid))
