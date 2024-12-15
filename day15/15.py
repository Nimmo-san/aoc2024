

filename = "day15/input.txt"

first_half, second_half = open(filename).read().split("\n\n")

grid = [list(line) for line in first_half.splitlines()]
moves = second_half.replace("\n", "")


rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "@":
            break
    else:
        continue
    break



for move in moves:
    dr = {'^': -1, 'v': 1}.get(move, 0)
    dc = {'<': -1, '>': 1}.get(move, 0)

    targets = [(row, col)]
    green = True
    cr = row
    cc = col
    while True:
        cr += dr
        cc += dc

        if grid[cr][cc] == '#':
            green = False
            break

        if grid[cr][cc] == 'O':
            targets.append((cr, cc))
        
        if grid[cr][cc] == '.':
            break

    if not green:
        continue

    grid[row][col] = '.'

    grid[row + dr][col + dc] = '@'

    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = 'O'
    
    row += dr
    col += dc


# for line in grid:
#     print(*line)

total = 0       

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'O':
            total += 100 * row + col

print(total)

    
