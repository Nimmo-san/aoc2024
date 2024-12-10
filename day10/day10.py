from pprint import pprint



filename = 'day10/input.txt'

with open(filename, mode='r') as file:
    grid = [[int(char) for char in line.strip()]for line in file]


rows = len(grid)
cols = len(grid[0])


trailheads = [(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == 0]
pprint(trailheads)