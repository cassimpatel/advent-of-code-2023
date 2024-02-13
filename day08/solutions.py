from math import lcm

def parse_input(input):
    ins = input.split('\n\n')[0]

    input = [x.split(', ') for x in input.replace(' = (', ', ').replace(')', '').split('\n\n')[1].split('\n')]
    graph = {}
    for [node, left, right] in input:
        graph[node] = [left, right]

    return ins, graph

def steps_taken(ins, graph, start, part2 = False):
    cur = start
    steps = 0
    stopping_cond = lambda x: (part2 and not x.endswith('Z')) or (not part2 and x != 'ZZZ')

    while stopping_cond(cur):
        cur = graph[cur][0] if ins[steps % len(ins)] == 'L' else graph[cur][1]
        steps += 1

    return steps
    
def day8_part1(input):
    ins, graph = parse_input(input)
    return steps_taken(ins, graph, 'AAA')

def day8_part2(input):
    ins, graph = parse_input(input)

    # get all the node ending in A
    starts = [x for x in graph if x.endswith('A')]
    
    steps = 1
    for start in starts:
        steps = lcm(steps, steps_taken(ins, graph, start, True))
    
    return steps

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day8_part1(example_input_1) == 6
    print(day8_part1(test_input))

    assert day8_part2(example_input_2) == 6
    print(day8_part2(test_input))