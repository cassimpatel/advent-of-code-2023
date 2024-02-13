def galaxy_distance_sums(grid, expansion_size = 2):
    # galaxies as (x, y) pairs
    galaxies = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.': continue
            galaxies.append((x, y))

    # compute the empty rows and columns
    empty_rows = []
    for y in range(len(grid)):
        if grid[y].count("#") == 0:
            empty_rows.append(y)
    empty_cols = []
    for x in range(len(grid[0])):
        if [row[x] for row in grid].count("#") == 0:
            empty_cols.append(x)

    # apply the expansion to each galaxy
    for i in range(len(galaxies)):
        (x, y) = galaxies[i]
        nx, ny = x, y

        for c in empty_cols:
            if c > x: break
            nx += expansion_size - 1

        for r in empty_rows:
            if r > y: break
            ny += expansion_size - 1

        galaxies[i] = (nx, ny)

    # calculate pairwise distances
    res = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            (x1, y1) = galaxies[i]
            (x2, y2) = galaxies[j]
            res += abs(x1 - x2) + abs(y1 - y2)

    return res

def day11_part1(input):
    input = input.split('\n')
    return galaxy_distance_sums(input)


def day11_part2(input, expansion_size):
    input = input.split('\n')
    return galaxy_distance_sums(input, expansion_size)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day11_part1(example_input) == 374
    print(day11_part1(test_input))

    assert day11_part2(example_input, 10) == 1030
    assert day11_part2(example_input, 100) == 8410
    print(day11_part2(test_input, 1000000))