def parse_input(input):
    # ignore unuseful info
    info = input.replace('Game ', '')

    # split each line by colon
    info = [x.split(': ') for x in info.split('\n')]

    # further split each lnie by clause then phrase
    for i in range(len(info)):
        info[i][1] = [[y.split() for y in x.split(', ')] for x in info[i][1].split('; ')]

    return info

def day2_part1(input):
    allowed = {
        'red'  : 12,
        'blue' : 14,
        'green': 13
    }

    input = parse_input(input)
    res = 0

    for [ID, rounds] in input:

        # flag for if the game is possible
        poss = True
        for round in rounds:

            # iterate over each num and colour present
            for [num, col] in round:

                # if val is more than allowed, break and set flag to exit
                if int(num) > allowed[col]:
                    poss = False
                    break
                if not poss: break
            if not poss: break

        # if still possible, add on the ID
        if poss:
            res += int(ID)

    return res

def day2_part2(input):
    input = parse_input(input)
    res = 0

    for [ID, rounds] in input:
        min_req = {'red': 0, 'blue': 0, 'green': 0}
        for round in rounds:
            # iterate over each num and colour present
            for [num, col] in round:
                min_req[col] = max(min_req[col], int(num))
        res += min_req['blue'] * min_req['red'] * min_req['green']

    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day2_part1(example_input) == 8
    print(day2_part1(test_input))

    assert day2_part2(example_input) == 2286
    print(day2_part2(test_input))