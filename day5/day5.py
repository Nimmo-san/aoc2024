
filename = 'day5/day5.txt'


with open(filename, mode='r') as file:
    sections = file.read().strip().split("\n\n")

    rules = [tuple(map(int, rule.split('|'))) for rule in sections[0].split('\n')]

    updates = [list(map(int, update.split(',')))  for update in sections[1].split('\n')]
