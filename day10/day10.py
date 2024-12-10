from collections import deque


filename = 'day10/input.txt'

with open(filename, mode='r') as file:
    grid = [[int(char) for char in line.strip()]for line in file]


rows = len(grid)
cols = len(grid[0])


# PART 1 and PART 2 USING BFS
trailheads = [(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == 0]
def sum_of_trail_heads(grid, row, col):
    queue = deque([(row, col)])
    seen = {(row, col)}

    traverse = 0

    while len(queue) > 0:
        nr, nc = queue.popleft()
        for dr, dc in [(nr - 1, nc), (nr, nc + 1), (nr + 1, nc), (nr, nc - 1)]:
            if dr < 0 or dc < 0 or dr >= rows or dc >= cols: continue  # noqa: E701
            if (grid[dr][dc] != grid[nr][nc] + 1): continue  # noqa: E701

            # Part 2
            # if (dr, dc) in seen: continue

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


# PART 1 and PART 2 USING DFS
def sum_of_trail_heads_using_dfs(grid):
    rows, cols = len(grid), len(grid[0])
    total = 0
    
    def dfs(cx, cy, seen):
        # if (cx, cy) in seen:
        #     return 0
        # seen.add((cx, cy))

        if grid[cx][cy] == 9:
            return 1
        
        score = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen:
                if grid[nx][ny] == grid[cx][cy] + 1:
                    score += dfs(nx, ny, seen)
        
        return score

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                seen = set()
                total += dfs(row, col, seen)
    return total

print(sum_of_trail_heads_using_dfs(grid))