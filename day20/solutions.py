def parse_input(input):
    input = input.split('\n')
    dest = {}
    types = {}

    # mark types and destinations for each module
    for line in input:
        [src, dsts] = line.split(' -> ')
        dsts = dsts.split(', ')

        if src[0] in '%&':
            typ, lbl = src[0], src[1:]
        else:
            typ, lbl = '', src

        types[lbl] = typ
        dest[lbl] = dsts

    # update remaining types and destinations for nodes that don't output
    for mod in dest:
        for nxt in dest[mod]:
            if nxt not in types:
                types[nxt] = ''
    for mod in types:
        if mod not in dest:
            dest[mod] = []

    # mark each flip flop module as off
    flips = {}
    for lbl in types:
        if types[lbl] != '%': continue
        flips[lbl] = 0

    # mark inputs for each conjunction module
    conjuncs = {}
    for lbl in types:
        if types[lbl] != '&': continue
        conjuncs[lbl] = {}
    for lbl in dest:
        for nxt in dest[lbl]:
            if nxt not in conjuncs: continue
            conjuncs[nxt][lbl] = 0
    
    return dest, types, flips, conjuncs

def count_low_highs(dests, types, flips, conjuncs):
    low, high = 0, 0

    for _ in range(1000):
        # start with broadcaster receiving low input
        pulses = pulses = [('broadcaster', 0)]

        while len(pulses) != 0:
            (module, inp) = pulses.pop(0)

            # update counts based on input
            if inp == 0: low += 1
            else: high += 1

            # deal with different types of modules, calculate output
            if types[module] == '%':
                if inp == 1: continue
                flips[module] = 1 - flips[module]
                out = flips[module]
            elif types[module] == '&':
                out = 1 if 0 in conjuncs[module].values() else 0
            else:
                out = inp

            for nxt in dests[module]:
                # print(f'{module} {out}-> {nxt}')
                pulses.append((nxt, out))

                # if the dest is a conjunction then update its corresponding input table
                if types[nxt] == '&':
                    conjuncs[nxt][module] = out

    return low, high

def day20_part1(input):
    dests, types, flips, conjuncs = parse_input(input)
    low, high = count_low_highs(dests, types, flips, conjuncs)
    return low * high

def find_inputs(dests, target):
    # find all the modules that lead into a target module
    res = []
    for module in dests:
        if target in dests[module]:
            res.append(module)
    return res

def day20_part2(input):
    dests, types, flips, conjuncs = parse_input(input)

    # find nodes that point to the node that points to rx, each has its own subgraph
    prev = find_inputs(dests, 'rx')[0]
    prev_prevs = find_inputs(dests, prev)
    min_pars = {x:-1 for x in prev_prevs}

    btnCount = 1
    while True:
        # found all of the cycles lengths: can abort
        if -1 not in min_pars.values():
            break

        # run procedure as usual
        pulses = [('broadcaster', 0)]
        while len(pulses) != 0:
            (module, inp) = pulses.pop(0)

            # we've found a pre-pre node receiving 0 i.e. found cycle len
            if module in prev_prevs and inp == 0:
                min_pars[module] = btnCount
            
            # deal with different types of modules
            if types[module] == '%':
                if inp == 1: continue
                flips[module] = 1 - flips[module]
                out = flips[module]
            elif types[module] == '&':
                out = 1 if 0 in conjuncs[module].values() else 0
            else:
                out = inp

            for nxt in dests[module]:
                # print(f'{module} {out}-> {nxt}')
                pulses.append((nxt, out))

                # if the dest is a conjunction then update its corresponding input table
                if types[nxt] == '&':
                    conjuncs[nxt][module] = out
        btnCount += 1

    res = 1
    for x in min_pars.values():
        res *= x

    return res

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day20_part1(example_input_1) == 32000000
    assert day20_part1(example_input_2) == 11687500
    print(day20_part1(test_input))

    print(day20_part2(test_input))