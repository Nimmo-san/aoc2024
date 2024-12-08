from pprint import pprint

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

for freq, locations in antennas.items():
    n = len(locations)
    if n < 2:
        continue


    for i in range(n):
        for j in range(i+1, n):

            r1, c1 = locations[i]
            r2, c2 = locations[j]

            mid_r = (r1+r2)/2
            mid_c = (c1+c2)/2

            if (r1 + r2) % 2 == 0 and (c1 + c2) % 2 == 0:
                antinode_r = int(mid_r)
                antinode_c = int(mid_c)

                dr = antinode_r - r1
                dc = antinode_c - c1

                antinode1 = (antinode_r - dr, antinode_c - dc)
                antinode2 = (antinode_r + dr, antinode_c + dc)

                if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                    antinodes.add(antinode2)
