from heapq import heappop, heappush

def default_get(dict, item, default):
    if item in dict:
        return dict[item]
    return default

def run_djikstra(grid, mindist = 1, maxdist = 3):
    n = len(grid)
    m = len(grid[0])

    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = [(0, 0, 0, -1)]
    seen = set()
    costs = {}

    while q:
        cost, x, y, dd = heappop(q)
        if (x, y) == (m-1, n-1):
            return cost
        if (x, y, dd) in seen:
            continue
        seen.add((x, y, dd))
        
        for dir in range(4):
            costInc = 0
            if dir == dd or (dir + 2) % 4 == dd: continue
            for dist in range(1, maxdist + 1):
                nx = x + DIRS[dir][0] * dist
                ny = y + DIRS[dir][1] * dist
                
                if not (0 <= ny < n and 0 <= nx < m): continue

                costInc += grid[ny][nx]
                if dist < mindist: continue
                nc = cost + costInc

                if costs.get((nx, ny, dir), 1e100) <= nc: continue
                costs[(nx, ny, dir)] = nc
                heappush(q, (nc, nx, ny, dir))

def day17_part1(input):
    grid = [[int(y) for y in x] for x in input.split('\n')]
    return run_djikstra(grid)

def day17_part2(input):
    grid = [[int(y) for y in x] for x in input.split('\n')]
    return run_djikstra(grid, 4, 10)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day17_part1(example_input) == 102
    print(day17_part1(test_input))

    assert day17_part2(example_input) == 94
    print(day17_part2(test_input))