
from pprint import pprint
filename = "day20/input.txt"


grid = [list(line) for line in open(filename).read().strip().split('\n')]

# pprint(grid)

rows = len(grid)
cols = len(grid[0])


sr,sc = 0,0
er,ec = 0,0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            sr,sc = i,j
            grid[i][j] = '.'
        elif grid[i][j] == 'E':
            er,ec = i,j
            grid[i][j] = '.'

print(sr,sc)
print(er,ec)

pprint(grid)
