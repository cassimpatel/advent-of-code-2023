def parse_input(input):
    input = input.replace(' map:', '').replace('seeds: ', '')
    [seeds, seed2soil, soil2fert, fert2wat, wat2ligh, ligh2temp, temp2humi, humi2loc] = input.split('\n\n')

    seeds = [int(x) for x in seeds.split()]
    true_map = []

    for map in (seed2soil, soil2fert, fert2wat, wat2ligh, ligh2temp, temp2humi, humi2loc):
        map = map.split('\n')
        true_map.append([[int(y) for y in x.split()] for x in map[1:]])

    return seeds, true_map

def location_lookup(seedNo, maps):
    val = seedNo
    for map in maps:
        for [dst_strt, src_strt, rng_lngth] in map:
            if val >= src_strt and val < src_strt + rng_lngth:
                val = dst_strt + (val - src_strt)
                break

    return val

def seed_lookup(locationNo, maps):
    val = locationNo
    for i in range(len(maps) - 1, -1, -1):
        for [dst_strt, src_strt, rng_lngth] in maps[i]:
            if val >= dst_strt and val < dst_strt + rng_lngth:
                val = src_strt + (val - dst_strt)
                break

    return val

def day5_part1(input):
    seeds, map = parse_input(input)
    locations = [location_lookup(x, map) for x in seeds]
    return min(locations)

def day5_part2(input):
    seeds, maps = parse_input(input)

    # create the ranges of seeds
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append([seeds[i], seeds[i+1]])

    # iterate up from the minimum location until we find one for which we have the corresponding seed
    loc = 0
    while True:
        seed = seed_lookup(loc, maps)
        for [rng_start, rng_len] in seed_ranges:
            if seed >= rng_start and seed < rng_start + rng_len:
                return loc
        if loc % 100000 == 0:
            print('Iteration:', loc)
        loc += 1

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day5_part1(example_input) == 35
    print(day5_part1(test_input))

    assert day5_part2(example_input) == 46
    print(day5_part2(test_input))

    # 59370573 too high