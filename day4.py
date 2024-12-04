
# (0, 1)   -> Right
# (0, -1)  -> Left
# (1, 0)   -> Down
# (-1, 0)  -> Up
# (1, 1)   -> Diagonal down-right
# (-1, -1) -> Diagonal up-left
# (1, -1)  -> Diagonal down-left
# (-1, 1)  -> Diagonal up-right

direction_choices = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

filename = "day4.txt"

data = []

with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]


word = 'XMAS'
word_length = len(word)
rows = len(grid)
cols = len(grid[0])
word_count = 0

for start_row in range(rows):
    for start_col in range(cols):
        for dx, dy in direction_choices:
            match = True

            for k in range(word_length):
                new_row = start_row + k * dx
                new_col = start_col + k * dy

                if not (0 <= new_row < rows and 0 <= new_col < cols) or grid[new_row][new_col] != word[k]:
                    match = False
                    break

            if match:
                word_count += 1

print(word_count)