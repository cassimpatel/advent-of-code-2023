def tilt(input, dir):
    n = len(input)
    m = len(input[0])

    if dir in 'NS':
        dir = 1 if dir == 'N' else -1
        settled = [0 if dir == 1 else n - 1] * m

        for y in range(n)[::dir]:
            for x in range(m):
                if input[y][x]   == '#':
                    settled[x] = y + dir
                elif input[y][x] == 'O':
                    input[y][x] = '.'
                    input[settled[x]][x] = 'O'
                    settled[x] += dir
    
    elif dir in 'EW':
        dir = 1 if dir == 'W' else -1
        settled = [0 if dir == 1 else m - 1] * n

        for x in range(m)[::dir]:
            for y in range(n):
                if input[y][x]   == '#':
                    settled[y] = x + dir
                elif input[y][x] == 'O':
                    input[y][x] = '.'
                    input[y][settled[y]] = 'O'
                    settled[y] += dir

    return input

def get_load(grid):
    n = len(grid)

    res = 0
    for y in range(n):
        res += (n - y) * grid[y].count('O')

    return res

def day14_part1(input):
    input = [[y for y in x] for x in input.split('\n')]
    input = tilt(input, 'N')

    return get_load(input)

def day14_part2(input):
    input = [[y for y in x] for x in input.split('\n')]
    NUM_CYCLES = 1000000000

    states = {}
    cycle_found = False
    cycle_no = 0

    while cycle_no < NUM_CYCLES:
        for dir in 'NWSE':
            input = tilt(input, dir)
        state = ('\n'.join(["".join(x) for x in input]))
        if not cycle_found and state in states:
            cycle_found = True
            cycle_len = cycle_no - states[state]
            cycles_left = (NUM_CYCLES - cycle_no) // cycle_len
            cycle_no += cycles_left * cycle_len
        states[state] = cycle_no
        cycle_no += 1

    return get_load(input)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day14_part1(example_input) == 136
    print(day14_part1(test_input))

    assert day14_part2(example_input) == 64
    print(day14_part2(test_input))