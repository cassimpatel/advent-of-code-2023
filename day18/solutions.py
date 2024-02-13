def calc_area(instructions):
    dirs = {'R': (0, 1), 'U': (-1, 0), 'D': (1, 0), 'L': (0, -1)}

    # calculate the vertices of the polygon, calculate total steps moved
    vertices = []
    y, x = (0, 0)
    tot_steps = 0
    for [dir, steps] in instructions:
        dy, dx = dirs[dir]
        y += dy * steps
        x += dx * steps
        tot_steps += int(steps)
        vertices.append((y, x))

    # run shoelace algorithm to calculate enclosed area
    n = len(vertices)
    sum1 = 0
    sum2 = 0
    for i in range(n-1):
        sum1 += vertices[i][0] * vertices[i+1][1]
        sum2 += vertices[i][1] * vertices[i+1][0]
    sum1 += vertices[n-1][0] * vertices[0][1]
    sum2 += vertices[0][0] * vertices[n-1][1]
    area = abs(sum1 - sum2) / 2

    # add on area encountered by steps themselves
    return int(area + tot_steps/2 + 1)

def day18_part1(input):
    input = [x.split()[:2] for x in input.split('\n')]
    input = [[x, int(y)] for [x, y] in input]

    return calc_area(input)

def day18_part2(input):
    dirs = ['R', 'D', 'L', 'U']

    # reformat to use hex clause instead
    input = [x.split()[2] for x in input.split('\n')]
    input = [[dirs[int(x[-2])], int(x[2:-2], 16)] for x in input]
 
    return calc_area(input)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day18_part1(example_input) == 62
    print(day18_part1(test_input))

    assert day18_part2(example_input) == 952408144115
    print(day18_part2(test_input))