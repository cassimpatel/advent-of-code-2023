from functools import cache

def parse_input(input):
    input = [x.split() for x in input.split('\n')]
    
    for i in range(len(input)):
        input[i][1] = tuple([int(x) for x in input[i][1].split(',')])

    return input

@cache
def count_arrangements(line, sizes, num_done = 0):
    if not line:
        return not sizes and not num_done

    num_sols = 0
    poss = '.#' if line[0] == '?' else line[0]
    for c in poss:
        if c == '#':
            num_sols += count_arrangements(line[1:], sizes, num_done + 1)
        elif num_done:
            if sizes and sizes[0] == num_done:
                num_sols += count_arrangements(line[1:], sizes[1:])
        else:
            num_sols += count_arrangements(line[1:], sizes)

    return num_sols

def day12_part1(input):
    input = parse_input(input)
    
    arrangements = [count_arrangements(line+'.', cond) for [line, cond] in input]
    return sum(arrangements)

def day12_part2(input):
    input = parse_input(input)
    for i in range(len(input)):
        [row, cond] = input[i]
        input[i][0] = '?'.join([row] * 5)
        input[i][1] = cond * 5

    arrangements = [count_arrangements(line+'.', cond) for [line, cond] in input]
    return sum(arrangements)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day12_part1(example_input) == 21
    print(day12_part1(test_input))

    assert day12_part2(example_input) == 525152
    print(day12_part2(test_input))