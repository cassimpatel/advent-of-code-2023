def extrapolate(arr):
    diff = [arr.copy()]

    while diff[-1].count(0) != len(diff[-1]):
        new_diff = [diff[-1][i+1] - diff[-1][i] for i in range(len(diff[-1]) - 1)]
        diff.append(new_diff)

    res = [x[-1] for x in diff]
    return sum(res)

def day9_part1(input):
    input = [[int(y) for y in x.split()] for x in input.split('\n')]
    extrapolations= [extrapolate(x) for x in input]

    return sum(extrapolations)

def day9_part2(input):
    input = [[int(y) for y in x.split()][::-1] for x in input.split('\n')]
    extrapolations = [extrapolate(x) for x in input]

    return sum(extrapolations)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day9_part1(example_input) == 114
    print(day9_part1(test_input))

    assert day9_part2(example_input) == 2
    print(day9_part2(test_input))