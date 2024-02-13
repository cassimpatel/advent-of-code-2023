def parse_and_pad(input):
    # split into a grid
    input = [[y for y in x] for x in input.split('\n')]

    # pad grid for simpler calculations
    input = [['.'] + x + ['.'] for x in input]
    input.append(['.'] * len(input[0]))
    input.insert(0, ['.'] * len(input[0]))

    return input
    
def search_num(grid, y, x):
    # if this cell isn't part of a number abort
    if not grid[y][x].isdigit():
        return 0

    # keep moving left to find the start of the num
    while grid[y][x-1].isdigit():
        x -= 1

    # work along the number and erase it as we go
    res = 0
    while grid[y][x].isdigit():
        res = res * 10 + int(grid[y][x])
        grid[y][x] = '.'
        x += 1
    
    return res

def day3_part1(input):
    input = parse_and_pad(input)
    n = len(input)
    m = len(input[0])

    res = 0
    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    for y in range(1, n - 1):
        for x in range(1, m - 1):
            c = input[y][x]

            # abort if this isn't a symbol cell
            if c.isdigit() or c == '.':
                continue

            # add up all the numbers in each direction if they can be found
            res += sum([search_num(input, y + dy, x + dx) for (dy, dx) in dirs])

    return res

def day3_part2(input):
    input = parse_and_pad(input)
    n = len(input)
    m = len(input[0])

    res = 0
    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    for y in range(1, n - 1):
        for x in range(1, m - 1):
            # abort if this isn't a cog
            if input[y][x] != '*':
                continue

            # take all part nums in each direction and filter to take valid ones
            part_nums = [search_num(input, y + dy, x + dx) for (dy, dx) in dirs]
            part_nums = [x for x in part_nums if x != 0]

            # take the product if exactly two nums are found
            if len(part_nums) != 2:
                continue
            res += part_nums[0] * part_nums[1]

    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day3_part1(example_input) == 4361
    print(day3_part1(test_input))

    assert day3_part2(example_input) == 467835
    print(day3_part2(test_input))