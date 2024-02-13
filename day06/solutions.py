from math import ceil

def day6_part1(input):
    input = input.replace('Time:', ''). replace('Distance:', '').split('\n')
    times = [int(x) for x in input[0].split() if x != ""]
    dists = [int(x) for x in input[1].split() if x != ""]

    res = 1
    for i in range(len(times)):
        r = ceil((times[i] + (times[i] ** 2 - 4 * dists[i]) ** 0.5) / 2) - 1
        res *= 2 * r - times[i] + 1

    return res

def day6_part2(input):
    input = input.replace(' ', '')
    return day6_part1(input)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day6_part1(example_input) == 288
    print(day6_part1(test_input))

    assert day6_part2(example_input) == 71503
    print(day6_part2(test_input))