def fill_pipes(grid):
    n = len(grid)
    m = len(grid[0])
    new_grid = [[0 for y in range(m)].copy() for x in range(n)]

    # find the S
    x, y = -1, -1
    for j in range(n):
        for i in range(m):
            if grid[j][i] == 'S':
                y, x = j, i
                break
        if (x, y) != (-1, -1): break

    # find the valid directions you can go from S 
    dir_options = []
    for (dx, dy, options) in [(-1, 0, 'LF-'), (1, 0, 'J7-'), (0, -1, '7F|'), (0, 1, 'LJ|')]:
        if y + dy < 0 or y + dy >= n: continue
        if x + dx < 0 or x + dx >= m: continue
        
        if grid[y+dy][x+dx] in options:
            dir_options.append((dx, dy))

    # fill in S with the correct label
    if (0, 1) in dir_options and (0, -1) in dir_options:
        grid[y][x] = '|'
    elif (1, 0) in dir_options and (-1, 0) in dir_options:
        grid[y][x] = '-'
    elif (0, -1) in dir_options and (1, 0) in dir_options:
        grid[y][x] = 'L'
    elif (0, -1) in dir_options and (-1, 0) in dir_options:
        grid[y][x] = 'J'
    elif (0, 1) in dir_options and (-1, 0) in dir_options:
        grid[y][x] = '7'
    elif (0, 1) in dir_options and (1, 0) in dir_options:
        grid[y][x] = 'F'
    (dx, dy) = dir_options[0]
    
    # follow round the grid and mark on alternative grid
    while new_grid[y][x] != 1:
        c = grid[y][x]
        if c == '|' or c == '-':
            dx, dy = dx, dy
        elif c == 'L':
            (dx, dy) = (1, 0) if (dx, dy) == (0, 1) else (0, -1)
        elif c == 'J':
            (dx, dy) = (-1, 0) if (dx, dy) == (0, 1) else (0, -1)
        elif c == '7':
            (dx, dy) = (-1, 0) if (dx, dy) == (0, -1) else (0, 1)
        elif c == 'F':
            (dx, dy) = (1, 0) if (dx, dy) == (0, -1) else (0, 1)

        new_grid[y][x] = 1
        x += dx
        y += dy

    return grid, new_grid

def day10_part1(input):
    grid = [[y for y in x] for x in input.split('\n')]
    grid, visited = fill_pipes(grid)

    visited = sum([x.count(1) for x in visited])
    return int(visited / 2)

def day10_part2(input):
    grid = [[y for y in x] for x in input.split('\n')]
    grid, visited = fill_pipes(grid)

    # move along the grid, switching inside (parity) based on |JL
    res = 0
    for y in range(len(grid)):
        # initially outside
        inside = False

        for x in range(len(grid[0])):

            c = grid[y][x]
            v = visited[y][x]

            # if this isn't a pipe, add 1 if we're currently inside
            if v == 0:
                res += 1 if inside else 0
                continue

            # if this is a vertical pipe, switch parity
            if c in '|JL':
                inside = not inside

    return res

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    example_input_3 = open('example_3.txt', 'r').read()
    example_input_4 = open('example_4.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day10_part1(example_input_1) == 8
    print(day10_part1(test_input))

    assert day10_part2(example_input_2) == 4
    assert day10_part2(example_input_3) == 8
    assert day10_part2(example_input_4) == 10
    print(day10_part2(test_input))