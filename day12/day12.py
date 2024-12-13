from pprint import pprint  # noqa: F401
from collections import deque  # noqa: F401

filename = "day12/input.txt"

with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]



# PART 1
def calculate_total_price_(grid):
    rows = len(grid)
    cols = len(grid[0])

    visited = set()

    def dfs(x, y, plant_type):
        stack = [(x, y)]
        area = 0
        # perimeter = 0
        edges = set()

        while stack:
            cx, cy = stack.pop()
            if (cx ,cy) in visited:
                continue

            visited.add((cx, cy))
            area += 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy

                edge = (min(cx, nx), min(cy, ny), dx, dy)
                print("Edge", edge, dx, dy)
                if 0 <= nx < rows and 0 <= ny < cols:
                    # if grid[nx][ny] == plant_type and (nx, ny) not in visited:
                    #     stack.append((nx, ny))
                    if grid[nx][ny] != plant_type and (nx, ny) not in visited:
                        edges.add(edge)
                        # perimeter += 1
                else:
                    edges.add(edge)
                    # perimeter += 1
        return area, len(edges) # perimeter
    
    total_price = 0
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                print("row, col, char", row, col, grid[row][col], )
                # area, perimeter = dfs(row, col, grid[row][col])
                # total_price += area * perimeter
                area, num_sides = dfs(row, col, grid[row][col])
                total_price += area * num_sides
                print("num_sides, total_price", num_sides, total_price)
    return total_price

print(calculate_total_price_(grid))