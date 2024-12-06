
# Debugging purposes
def print_grid(grid, guard_pos, facing_direction):
    symbols = ['^', '>', 'v', '<']
    temp_grid = [row[:] for row in grid]
    temp_grid[guard_pos[0]][guard_pos[1]] = symbols[facing_direction]
    for row in temp_grid:
        print("".join(row))
    print("\n")

filename = "day6/day6.txt"

with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

rows = len(grid)
cols = len(grid[0])

start_pos = None
facing_direction = 0

for row in range(rows):
    for col in range(cols):
        if grid[row][col] in direction_map:
            start_pos = (row, col)
            facing_direction = direction_map[grid[row][col]]
            grid[row][col] = '.'
            break
    if start_pos:
        break

current_pos = start_pos
visited = set()
visited.add(current_pos)
step_limit = 100000
steps = 0
next_pos = current_pos

while (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):

    # print(f"Step: {steps}, Current Pos: {current_pos}, Facing: {facing_direction}, Next Pos towards: {directions[facing_direction]}")

    # print_grid(grid, current_pos, facing_direction)

    dr, dc = directions[facing_direction]
    next_pos = (current_pos[0] + dr, current_pos[1] + dc)

    if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols) or grid[next_pos[0]][next_pos[1]] == '#':
        facing_direction = (facing_direction + 1) % 4
        # print(f"Blocked. Turned to Facing: {facing_direction}")
    else:
        current_pos = next_pos
        visited.add(current_pos)
        # print(f"Moved to {current_pos}")

    # steps += 1
print(len(visited))
