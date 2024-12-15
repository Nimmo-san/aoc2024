import copy

filename = "day15/input.txt"

first_half, second_half = open(filename).read().split("\n\n")


char_replace = {
    '#': '##',
    'O': '[]',
    '.': '..',
    '@': '@.'
}

grid_part1 = [list(line) for line in first_half.splitlines()]
grid_part2 = [list(''.join(char_replace[char] for char in line)) for line in first_half.splitlines()]
moves = second_half.replace("\n", "")

# print('\n'.join(grid_part2))

# exit(0)

def part1(grid, moves):
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

    # total = 0
    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 'O':
    #             total += 100 * row + col

    return sum(100 * row + col for row in range(rows) for col in range(cols) if grid[row][col] == 'O')


def part2(grid, moves):
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "@":
                break
        else:
            continue
        break
    
    # print("initial pos of robot",row, col)
    for move in moves:
        dr = {'^': -1, 'v': 1}.get(move, 0)
        dc = {'<': -1, '>': 1}.get(move, 0)
        targets = [(row, col)]
        green = True
        for cr, cc in targets:
            nr = cr + dr
            nc = cc + dc
            
            if (nr, nc) in targets:
                continue

            char = grid[nr][nc]
            if char == '#':
                green = False
                break

            if char == '[':
                targets.append((nr, nc))
                targets.append((nr, nc + 1))
            
            if char == ']':
                targets.append((nr, nc))
                targets.append((nr, nc - 1))
        if not green:
            continue
        
        grid_copy = copy.deepcopy(grid)
        # print(grid[row][col])
        grid[row][col] = "."
        grid[row + dr][col + dc] == '@'

        for br, bc in targets[1:]:
            grid[br][bc] = "."
        
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = grid_copy[br][bc]

        row += dr
        col += dc

    
    return sum(100 * row + col for row in range(rows) for col in range(cols) if grid[row][col] == '[')

print(part2(grid_part2, moves))
        
