from pprint import pprint


filename = "day16/input.txt"

    
grid = [list(line) for line in open(filename).read().strip().split('\n')]


rows = len(grid)
cols = len(grid[0])

# print(grid)
sr,sc = 0, 0
er,ec = 0, 0

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'S':
            sr, sc = row, col
            grid[row][col] = '.'
        elif grid[row][col] == 'E':
            er, ec = row, col
            grid[row][col] = '.'


