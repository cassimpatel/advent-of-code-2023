def num_plots(grid, steps):
    n = len(grid)
    m = len(grid[0])

    sy, sx = 0, 0
    fnd = False
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 'S':
                sy = y
                sx = x
                fnd = True
                break
        if fnd: break

    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    res = 0
    queue = [(sy, sx)]
    vis = set()
    prev_vis = set()

    for i in range(steps + 1):
        new_queue = []
        new_vis = set()

        for (y, x) in queue:
            if (y, x) in vis or (y, x) in prev_vis or grid[y % n][x % m] == '#': continue
            vis.add((y, x))
            new_vis.add((y, x))
            res += 1 if steps % 2 == i % 2 else 0

            for (dy, dx) in neighbours:
                new_queue.append((y + dy, x + dx))
        queue = new_queue
        vis, prev_vis = new_vis, vis

    return res

def print_progress_bar (iteration, total, length = 50):
    percent      = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar          = '█' * filledLength + '-' * (length - filledLength)

    print(f'\rSimulation progress |{bar}| {percent}% ({iteration} of {total}) completed', end = '\r')
    if iteration >= total: 
        print('')
    
def day21_part1(input, steps=64):
    grid = [[y for y in x] for x in input.split('\n')]
    return num_plots(grid, steps)
    

def day21_part2(input, steps):
    grid = [[y for y in x] for x in input.split('\n')]
    width = len(grid)
    rem = steps % width
    
    v1 = num_plots(grid, rem)
    v2 = num_plots(grid, rem + width)
    v3 = num_plots(grid, rem + width * 2)

    a = (v1 - 2 * v2 + v3) // 2
    b = (-3 * v1 + 4 * v2 - v3) // 2
    c = v1
    n = steps // width
    res = a * n * n + b * n + c

    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day21_part1(example_input, 6) == 16
    print(day21_part1(test_input))

    print(day21_part2(test_input, 26501365))