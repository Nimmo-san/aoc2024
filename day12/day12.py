from pprint import pprint



filename = "day12/input.txt"

with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]



pprint(grid)