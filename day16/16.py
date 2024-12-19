
import heapq
from collections import deque


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


def dijkstra_with_rotation_part1(grid, start, end):
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0, 1))
    
    visited = set()
    
    while pq:

        score, x, y, dr, dc = heapq.heappop(pq)

        visited.add((x, y, dr, dc))

        if (x, y) == end:
            return score

        for new_score, nr, nc, ndr, ndc in [(score + MOVE_COST, x + dr, y + dc, dr, dc), (score + ROTATE_COST, x, y, dc, -dr), (score + ROTATE_COST, x, y, -dc, dr)]:
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
    

def dijkstra_with_rotation_part2(grid, start, end):
    pq = []
    lowest_score = {(start[0], start[1], 0, 1): 0}
    backtracking = {}
    last_state = set()
    best_score = float('inf')
    heapq.heappush(pq, (0, start[0], start[1], 0, 1, None, None, None, None))
    
    while pq:
        score, x, y, dr, dc, pr, pc, pdr, pdc = heapq.heappop(pq)

        if score > lowest_score.get((x, y, dr, dc), float('inf')):
            continue
        lowest_score[(x, y, dr, dc)] = score

        if (x, y) == end:
            if score > best_score:
                break
            best_score = score
            last_state.add((x, y, dr, dc))

        if (x, y, dr, dc) not in backtracking:
            backtracking[(x, y, dr, dc)] = set()
        
        backtracking[(x, y, dr, dc)].add((pr, pc, pdr, pdc))
        for new_score, nr, nc, ndr, ndc in [(score + MOVE_COST, x + dr, y + dc, dr, dc), (score + ROTATE_COST, x, y, dc, -dr), (score + ROTATE_COST, x, y, -dc, dr)]:
            if grid[nr][nc] == '#':
                continue
            if score > lowest_score.get((nr, nc, ndr, ndc), float('inf')):
                continue

            heapq.heappush(pq, (new_score, nr, nc, ndr, ndc, x, y, dr, dc))
        
    seen_states = set(last_state)
    all_states = deque(last_state)

    while all_states:
        value = all_states.popleft()
        for last in backtracking.get(value, []):
            if last in seen_states:
                continue
            x, y, _, _ = last
            seen_states.add((x, y))
            all_states.append(last)
    
    return len(seen_states)


start, end = parse_maze(grid)

# part 1
# min_score = dijkstra_with_rotation_part1(grid, start, end)
# print(min_score)

# part 2
score = dijkstra_with_rotation_part2(grid, start, end)
print(score)

