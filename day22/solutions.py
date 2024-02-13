def get_brick_supports(input):
    max_x = max([x[3] for x in input])
    max_y = max([x[4] for x in input])

    heights = [[1 for x in range(max_x+1)].copy() for y in range(max_y+1)]
    support = [[-1 for x in range(max_x+1)].copy() for y in range(max_y+1)]
    supported_by = {i:set() for i in range(len(input))}
    supports = {i:set() for i in range(-1, len(input))}

    for i in range(len(input)):
        [x1, y1, z1, x2, y2, z2] = input[i]
        height = 0

        # find height at which block rests
        for y in range(x1, x2 + 1):
            for x in range(y1, y2 + 1):
                height = max(height, heights[y][x])
   

        for y in range(x1, x2 + 1):
            for x in range(y1, y2 + 1):

                # if we rest on a block, update the supported by and supports graph
                if heights[y][x] == height:
                    supported_by[i].add(support[y][x])
                    supports[support[y][x]].add(i)

                # update new height and supporting matrix
                heights[y][x] = height + z2 - z1 + 1
                support[y][x] = i

    return supports, supported_by

def get_single_supporters(input, supports, supported_by):
    res = []

    for i in range(len(input)):
        # if this block doesn't support anything it can be disintegrated
        if supports[i] == set():
            res.append(i)
            continue

        # for each brick supported, is there another brick supporting it?
        can_remove = [supported_by[nxt] != set([i]) for nxt in supports[i]]
        if all(can_remove):
            res.append(i)

    return res

def day22_part1(input):
    # parse input, sort for lowest blocks first, calculate support graph
    input = [[int(y) for y in x.split(',')] for x in input.replace('~', ',').split('\n')]
    input.sort(key=lambda x: x[2])
    supports, supported_by = get_brick_supports(input)

    # generate bricks that may be disintegrated
    single_supporters = get_single_supporters(input, supports, supported_by)
    return len(single_supporters)
    
def count_falls(supports, supported_by, brick):

    # do a BFS: bricks that aren't additionally supported and would fall are added to the queue
    queue = [brick]
    fallen = set([])

    while queue:
        brick = queue.pop(0)
        fallen.add(brick)

        # add each block brick is supporting only if that blocks supporting blocks have all fallen
        for nxt in supports[brick]:
            nxt_supports = [x for x in supported_by[nxt] if x not in fallen]
            if len(nxt_supports) != 0: continue
            queue.append(nxt)

    # minus 1 to account for counting only other bricks
    return len(fallen) - 1

def day22_part2(input):
    # parse input, sort for lowest blocks first, calculate support graph
    input = [[int(y) for y in x.split(',')] for x in input.replace('~', ',').split('\n')]
    input.sort(key=lambda x: x[2])
    supports, supported_by = get_brick_supports(input)

    # generate number of other bricks to fall if each brick was disintegrated
    fall_counts = [count_falls(supports, supported_by, i) for i in range(len(input))]
    return sum(fall_counts)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day22_part1(example_input) == 5
    print(day22_part1(test_input))

    assert day22_part2(example_input) == 7
    print(day22_part2(test_input))