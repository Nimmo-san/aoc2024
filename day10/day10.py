from collections import deque


filename = 'day10/input.txt'

with open(filename, mode='r') as file:
    grid = [[int(char) for char in line.strip()]for line in file]


rows = len(grid)
cols = len(grid[0])


# USING BFS
trailheads = [(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == 0]
def sum_of_trail_heads(grid, row, col):
    queue = deque([(row, col)])
    seen = {(row, col)}

    traverse = 0

    while len(queue) > 0:
        nr, nc = queue.popleft()
        for dr, dc in [(nr - 1, nc), (nr, nc + 1), (nr + 1, nc), (nr, nc - 1)]:
            if dr < 0 or dc < 0 or dr >= rows or dc >= cols: continue
            if grid[dr][dc] != grid[nr][nc] + 1: continue

            if (dr, dc) in seen: continue

            seen.add((dr, dc))

            if grid[dr][dc] == 9:
                traverse += 1
            else:
                queue.append((dr, dc))
    return traverse

total = 0
for row, col in trailheads:
    total += sum_of_trail_heads(grid, row, col)

print(total)