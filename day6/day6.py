from pprint import pprint

filename = "day6/day6.txt"

with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]



pprint(grid)