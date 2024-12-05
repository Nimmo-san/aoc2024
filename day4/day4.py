
# (0, 1)   -> Right
# (0, -1)  -> Left
# (1, 0)   -> Down
# (-1, 0)  -> Up
# (1, 1)   -> Diagonal down-right
# (-1, -1) -> Diagonal up-left
# (1, -1)  -> Diagonal down-left
# (-1, 1)  -> Diagonal up-right


filename = "day4/day4.txt"


with open(filename, mode='r') as file:
    grid = [list(line.strip()) for line in file]


# word = 'XMAS'
# word_length = len(word)
# data = []
rows = len(grid)
cols = len(grid[0])
# word_count = 0
# direction_choices = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# for start_row in range(rows):
#     for start_col in range(cols):
#         for dx, dy in direction_choices:
#             match = True

#             for k in range(word_length):
#                 new_row = start_row + k * dx
#                 new_col = start_col + k * dy

#                 if not (0 <= new_row < rows and 0 <= new_col < cols) or grid[new_row][new_col] != word[k]:
#                     match = False
#                     break

#             if match:
#                 word_count += 1

# print(word_count)


""" Searching for MAS """

mas_count = 0

directions = {
    "tlbr": [(1, 1), (-1, -1)],
    "trbl": [(1, -1), (-1, 1)]
}

for row in range(rows):
    for col in range(cols):

        if grid[row][col] != 'A':
            continue
        
        valid = True
        for dir_name, (dir1, dir2) in directions.items():
            dx1, dy1 = dir1
            dx2, dy2 = dir2
            
            top_mas = (row + dx1, col + dy1)
            bottom_mas = (row + dx2, col + dy2)

            # print(top_mas, bottom_mas)
            if not (
                0 <= top_mas[0] < rows and 0 <= top_mas[1] < cols and
                0 <= bottom_mas[0] < rows and 0 <= bottom_mas[1] < cols
            ):
                valid = False
                break
            
            if (grid[top_mas[0]][top_mas[1]], grid[bottom_mas[0]][bottom_mas[1]]) not in [('M', 'S'), ('S', 'M')]:
                # print(grid[top_mas[0]][top_mas[1]], grid[bottom_mas[0]][bottom_mas[1]])
                valid = False
                break

        if valid:
            mas_count += 1


print(mas_count)