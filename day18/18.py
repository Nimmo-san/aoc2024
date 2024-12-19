from collections import deque
from pprint import pprint

filename = "day18/input.txt"



# actual input size
# N = 7# 0

# test case
# N = 7

# data = open(filename).read().strip()

# grid_to_consider = [['.' for col in range(N)] for row in range(N)]


# for i,line in enumerate(data.split('\n')):
   #  print(i, line.split(','))


# TEST CASE
#size = 6
#byte_pull = 12

# ACTUAL 
size = 70
byte_pull = 1024

grid = [[0] * ( size + 1) for _ in range(size + 1)]

ins = [list(map(int, line.split(','))) for line in open(filename).read().strip().split('\n')]

for col,row in ins[:byte_pull]:
    grid[row][col] = 1

#pprint(grid)

queue= deque([(0, 0, 0)])
visited = {(0, 0)}
ok = True
while queue:
    x, y, d, = queue.popleft()
    for nx,ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
         if nx < 0 or ny < 0 or nx > size or ny > size:
             continue
         if grid[nx][ny] == 1:
             continue
         if (nx, ny) in visited:
             continue
         if nx == ny == size:
             #print(d+ 1)
             ok = False
             break

         visited.add((nx, ny))
         queue.append((nx, ny, d + 1))
    if not ok:
        print(x, y)
