def hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256

    return res

def day15_part1(input):
    input = input.split(',')
    hashes = [hash(x) for x in input]

    return sum(hashes)

def searchForMatch(hashmap, label):
    hash_index = hash(label)
    
    # simple search for index if label exists in hashmap entry
    for i in range(len(hashmap[hash_index])):
        if hashmap[hash_index][i][0] == label:
            return i

    return -1

def day15_part2(input):
    input = input.split(',')
    hashmap = [[].copy() for x in range(256)]

    for line in input:
        if line.endswith('-'):
            # remove the label from the hashmap entry if it exists
            lab = line[:-1]
            hash_ind = hash(lab)
            search_ind = searchForMatch(hashmap, lab)
            if search_ind == -1: continue
            del hashmap[hash_ind][search_ind]
        else:
            # look for if the label exists in the hash map entry
            [lab, val] = line.split('=')
            hash_ind = hash(lab)
            search_ind = searchForMatch(hashmap, lab)
            if search_ind == -1:
                # append to end, the label doesn't already exist
                hashmap[hash_ind].append([lab, val])
            else:
                # overwrite existing label with new one's value
                hashmap[hash_ind][search_ind] = [lab, val]

    res = 0
    for box in range(256):
        for lensNo in range(len(hashmap[box])):
            [lab, val] = hashmap[box][lensNo]
            res += (box + 1) * (lensNo + 1) * int(val)

    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day15_part1(example_input) == 1320
    print(day15_part1(test_input))

    assert day15_part2(example_input) == 145
    print(day15_part2(test_input))