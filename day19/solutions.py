from math import prod
import copy

def parse_input(input):
    [ins, parts] = [x.split('\n') for x in input.split('\n\n')]

    true_ins = {}
    for i in range(len(ins)):
        line = ins[i].replace('}', '')
        [lab, conds] = line.split('{')
        conds = conds.split(',')
        true_ins[lab] = conds

    for i in range(len(parts)):
        pts = parts[i].replace('{', '').replace('}', '').replace('=', '')
        [xpt, mpt, apt, spt] = pts.split(',')
        parts[i] = {'x': int(xpt[1:]), 'm': int(mpt[1:]), 'a': int(apt[1:]), 's': int(spt[1:])}

    return true_ins, parts

def get_result(ins, part):
    cur_workflow = 'in'

    while cur_workflow not in ['A', 'R']:
        fnd = False

        for rule in ins[cur_workflow][:-1]:
            cond, res = rule.split(':')
            if eval(f'part["{cond[0]}"]{cond[1:]}') == True:
                cur_workflow = res
                fnd = True
                break
        
        if fnd: continue

        cur_workflow = ins[cur_workflow][-1]

    return cur_workflow

def day19_part1(input):
    ins, parts = parse_input(input)

    parts = [x for x in parts if get_result(ins, x) == 'A']
    res   = sum([sum(x.values()) for x in parts])
    return res

def split_ranges(ranges, cond):
    # generate a left and right range as a copy
    lRange, rRange = copy.deepcopy(ranges), copy.deepcopy(ranges)
    lab, op, val = cond[0], cond[1], int(cond[2:])

    # modify left and right ranges depending on condition to break
    if op == '<':
        lRange[lab][1] = val
        rRange[lab][0] = val
    else:
        lRange[lab][0] = val + 1
        rRange[lab][1] = val + 1

    return lRange, rRange

def find_combs(ins, workflow, ranges):
    # terminating conditions: if R then 0, otherwise product of range lengths
    if workflow == 'R':
        return 0
    if workflow == 'A':
        rangeLen = [b-a for [a,b] in ranges.values()]
        return prod(rangeLen)

    # for each rule, break ranges, recursively calculate combinations, and move on using remainding range
    res = 0
    for rule in ins[workflow][:-1]:
        cond, nxt = rule.split(':')
        cur_range, ranges = split_ranges(ranges, cond)
        res += find_combs(ins, nxt, cur_range)

    # add on the default rule at the end of the workflow
    res += find_combs(ins, ins[workflow][-1], ranges)
    return res

def day19_part2(input):
    ins, _ = parse_input(input)

    # calculate starting ranges and then combinations
    ranges = {'x': [1, 4001], 'm': [1, 4001], 'a': [1, 4001], 's': [1, 4001]}
    res = find_combs(ins, 'in', ranges)

    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day19_part1(example_input) == 19114
    print(day19_part1(test_input))

    assert day19_part2(example_input) == 167409079868000
    print(day19_part2(test_input))