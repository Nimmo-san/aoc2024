from pprint import pprint
from collections import deque

filename = "day8/day8.txt"

with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]


rows = len(grid)
cols = len(grid[0])


antennas = {}

for row in range(rows):
    for col in range(cols):
        if grid[row][col] != '.':
            freq = grid[row][col]
            if freq not in antennas:
                antennas[freq] = []
            antennas[freq].append((row, col))


antinodes = set()

# FOR PART 1
# for freq, positions in antennas.items():
#     n = len(positions)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             loc_diff = (
#                 positions[i][0] - positions[j][0],
#                 positions[i][1] - positions[j][1]
#             )
#             # print(loc_diff)
#             for loc in (positions[i], positions[j]):
#                 new_loc = (loc[0] + loc_diff[0], loc[1] + loc_diff[1])

#                 if 0 <= new_loc[0] < rows and 0 <= new_loc[1] < cols and grid[new_loc[0]][new_loc[1]] != freq:
#                     antinodes.add(new_loc)
#                     grid[new_loc[0]][new_loc[1]] = '#'

#                 # maybe consider a neg
#                 new_loc_neg = (loc[0] - loc_diff[0], loc[1] - loc_diff[1])
#                 if 0 <= new_loc_neg[0] < rows and 0 <= new_loc_neg[1] < cols and grid[new_loc_neg[0]][new_loc_neg[1]] != freq:
#                     antinodes.add(new_loc_neg)
#                     grid[new_loc_neg[0]][new_loc_neg[1]] = '#'



# FOR PART 2
for freq, positions in antennas.items():
    n = len(positions)
    for i in range(n - 1):
        for j in range(i + 1, n):
            loc_diff = (
                positions[i][0] - positions[j][0],
                positions[i][1] - positions[j][1]
            )
            visited = set()
            queue = deque([positions[i], positions[j]])

            # print(loc_diff)
            while queue:
                loc = queue.popleft()
                new_loc = (loc[0] + loc_diff[0], loc[1] + loc_diff[1])

                if 0 <= new_loc[0] < rows and 0 <= new_loc[1] < cols and new_loc not in visited:
                    visited.add(new_loc)
                    queue.append(new_loc)
                    antinodes.add(new_loc)
                    grid[new_loc[0]][new_loc[1]] = '#'

                # maybe consider a neg
                new_loc_neg = (loc[0] - loc_diff[0], loc[1] - loc_diff[1])
                if 0 <= new_loc_neg[0] < rows and 0 <= new_loc_neg[1] < cols and new_loc_neg not in visited:
                    visited.add(new_loc_neg)
                    queue.append(new_loc_neg)
                    antinodes.add(new_loc_neg)
                    grid[new_loc_neg[0]][new_loc_neg[1]] = '#'


print(len(antinodes))