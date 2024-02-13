def day4_part1(input):
    input = [x.split(': ')[1] for x in input.split('\n')]
    input = [[y.split() for y in x.split(' | ')] for x in input]

    res = 0
    for [winning, mine] in input:
        crossover = len(set(mine).intersection(set(winning)))
        if crossover != 0:
            res += 2 ** (crossover - 1)

    return res

def day4_part2(input):
    input = [x.split(': ')[1] for x in input.split('\n')]
    input = [[y.split() for y in x.split(' | ')] for x in input]

    cards = [1 for x in range(len(input))]

    for i in range(len(input)):
        [winning, mine] = input[i]
        crossover = len(set(mine).intersection(set(winning)))
        for j in range(i + 1, i + 1 + crossover):
            if j >= len(cards):
                break
            cards[j] += cards[i]

    return sum(cards)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day4_part1(example_input) == 13
    print(day4_part1(test_input))

    assert day4_part2(example_input) == 30
    print(day4_part2(test_input))