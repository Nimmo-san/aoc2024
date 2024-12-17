import heapq

filename = "day16/input.txt"

    
grid = [list(line) for line in open(filename).read().strip().split('\n')]


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ROTATE_COST = 1000
MOVE_COST = 1


def parse_maze(grid):
    start = None
    end = None
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
        else:
            continue
    return start, end


def dijkstra_with_rotation(grid, start, end):
    # rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0, 1))
    
    visited = set()
    
    while pq:

        score, x, y, dr, dc = heapq.heappop(pq)

        visited.add((x, y, dr, dc))

        if (x, y) == end:
            return score
            break

        for new_score, nr, nc, ndr, ndc in [(score + 1, x + dr, y + dc, dr, dc), (score + 1000, x, y, dc, -dr), (score + 1000, x, y, -dc, dr)]:
            if grid[nr][nc] == '#':
                continue
            if (nr, nc, ndr, ndc) in visited:
                continue

            heapq.heappush(pq, (new_score, nr, nc, ndr, ndc))
        # print(pq)
        # score, x, y, direction = heapq.heappop(pq)
        
        # if (x, y) == end:
        #     return score
        
        # if (x, y, direction) in visited:
        #     continue
        # visited.add((x, y, direction))
        
        # fr
        # dx, dy = DIRECTIONS[direction]
        # nx, ny = x + dx, y + dy
        # if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
        #     heapq.heappush(pq, (score + MOVE_COST, nx, ny, direction))
        
        # CW
        # new_direction_cw = (direction - 1 + 4) % 4
        # heapq.heappush(pq, (score + ROTATE_COST, x, y, new_direction_cw))
        
        # Counter cw
        # new_direction_ccw = (direction + 1) % 4
        # heapq.heappush(pq, (score + ROTATE_COST, x, y, new_direction_ccw))
    

start, end = parse_maze(grid)
min_score = dijkstra_with_rotation(grid, start, end)
print(min_score)
