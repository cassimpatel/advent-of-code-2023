def trace(grid, y, x, dy, dx, vis):
    n = len(grid)
    m = len(grid[0])

    while 0 <= x < m and 0 <= y < n and (y, x, dy, dx) not in vis:
        vis.add((y, x, dy, dx))

        c = grid[y][x]
        if c ==  '|' and dx:
            trace(grid, y + 1, x, 1, 0, vis)
            trace(grid, y - 1, x, -1, 0, vis)
            break  
        elif c == '-' and dy:
            trace(grid, y, x + 1, 0, 1, vis)
            trace(grid, y, x - 1, 0, -1, vis)
            break
        elif c == '/':
            dx, dy = -dy, -dx
        elif c == '\\':
            dx, dy = dy, dx
        
        y += dy
        x += dx

def printGrid(vis, n, m):
    for y in range(n):
        for x in range(m):
            fnd = False
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (y, x, dy, dx) in vis:
                        fnd = True
                        break
                if fnd: break
            if not fnd:
                print('.', end='')
            else:
                print('#', end='')

        print()

def day16_part1(input, sy=0, sx=0, sdy=0, sdx=1):
    grid = input.split('\n')
    
    n = len(grid)
    m = len(grid[0])
    vis = set([])

    trace(grid, sy, sx, sdy, sdx, vis)

    vis = set([(y, x) for (y, x, dy, dx) in vis])
    return len(vis)

def day16_part2(input):
    grid = input.split('\n')
    n = len(grid)
    m = len(grid)

    res = 0
    for y in range(n):
        res = max(res, day16_part1(input, y, 0, 0, 1))
        res = max(res, day16_part1(input, y, m - 1, 0, -1))
    for x in range(m):
        res = max(res, day16_part1(input, 0, x, 1, 0))
        res = max(res, day16_part1(input, n - 1, x, -1, 0))

    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day16_part1(example_input) == 46
    print(day16_part1(test_input))

    assert day16_part2(example_input) == 51
    print(day16_part2(test_input))