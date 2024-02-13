def counter(iterable):
    cnt = {}
    for x in iterable:
        if x not in cnt:
            cnt[x] = 0
        cnt[x] += 1
    return cnt

def handVal(hand):
    cnt = counter(hand)
    cnt = counter(cnt.values())
    
    hand_type = -1
    if 5 in cnt:
        hand_type = 0
    elif 4 in cnt:
        hand_type = 1
    elif 3 in cnt and 2 in cnt:
        hand_type = 2
    elif 3 in cnt:
        hand_type = 3
    elif 2 in cnt and cnt[2] == 2:
        hand_type = 4
    elif 2 in cnt:
        hand_type = 5
    else:
        hand_type = 6

    vals = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for i, c in enumerate(vals):
        hand = hand.replace(c, chr(ord('a') + i))

    return (hand_type, hand)

def handVal2(hand):
    vals = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    best_type = 7
    for c in vals:
        hand_copy = hand.replace('J', c)
        cnt = counter(hand_copy)
        cnt = counter(cnt.values())
    
        hand_type = -1
        if 5 in cnt:
            hand_type = 0
        elif 4 in cnt:
            hand_type = 1
        elif 3 in cnt and 2 in cnt:
            hand_type = 2
        elif 3 in cnt:
            hand_type = 3
        elif 2 in cnt and cnt[2] == 2:
            hand_type = 4
        elif 2 in cnt:
            hand_type = 5
        else:
            hand_type = 6

        best_type = min(best_type, hand_type)

    for i, c in enumerate(vals):
        hand = hand.replace(c, chr(ord('a') + i))

    return (best_type, hand)
    

def day7_part1(input):
    input = [x.split() for x in input.split('\n')]

    # add the hand value onto each hand and sort by this
    input = [x + [handVal(x[0])] for x in input]
    input.sort(key = lambda x: x[2], reverse=True)

    res = 0
    for i, v in enumerate(input):
        res += int(v[1]) * (i + 1)

    return res

def day7_part2(input):
    input = [x.split() for x in input.split('\n')]

    # add the hand value onto each hand and sort by this
    input = [x + [handVal2(x[0])] for x in input]
    input.sort(key = lambda x: x[2], reverse=True)

    res = 0
    for i, v in enumerate(input):
        res += int(v[1]) * (i + 1)

    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day7_part1(example_input) == 6440
    print(day7_part1(test_input))

    assert day7_part2(example_input) == 5905
    print(day7_part2(test_input))