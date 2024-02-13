def day1_part1(input):
    res =  0

    # grab all digits from line, use first and last to form cal val
    for line in input.split('\n'):
        nums = [int(x) for x in line if x.isdigit()]
        res += nums[0] * 10 + nums[-1]

    return res

def day1_part2(input):
    nums = {
        'one'  : "1",
        'two'  : "2",
        'three': "3",
        'four' : "4",
        'five' : "5",
        'six'  : "6",
        'seven': "7",
        'eight': "8",
        'nine' : "9",
    }

    # replace each number by the name then value then name incase the name forms part of another named number e.g. one => one1one
    for x in nums:
        input = input.replace(x, f'{x}{nums[x]}{x}')

    # continue process as usual from part 1
    return day1_part1(input)

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day1_part1(example_input_1) == 142
    print(day1_part1(test_input))

    assert day1_part2(example_input_2) == 281
    print(day1_part2(test_input))