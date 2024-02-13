def findReflection(grid):
    n = len(grid)
    m = len(grid[0])

    # try to find a vertical reflection
    for x in range(0, m-1):
        found_reflection = True
        numToCheck = min(x + 1, m - x - 1)

        for colDiff in range(numToCheck):
            
            lCol = x - colDiff
            rCol = x + colDiff + 1
            for y in range(n):
                if grid[y][lCol] != grid[y][rCol]:
                    found_reflection = False
                    break
            if not found_reflection: break
        if found_reflection:
            return (0, x + 1)

    # try to find a horizontal reflection
    for y in range(0, n-1):
        found_reflection = True
        numToCheck = min(y + 1, n - y - 1)

        for rowDiff in range(numToCheck):
            lRow = y - rowDiff
            rRow = y + rowDiff + 1
            for x in range(m):
                if grid[lRow][x] != grid[rRow][x]:
                    found_reflection = False
                    break
            if not found_reflection: break

        if found_reflection:
            return (y + 1, 0)

    # x reflection then y reflection
    return 0, 0

def findSmudgedReflection(grid):
    n = len(grid)
    m = len(grid[0])
    prevSol = findReflection(grid)

    # try to find a vertical reflection
    for x in range(0, m-1):
        # ignore this potential reflection this was the previous solution for part 1
        if prevSol == (0, x+1):
            continue

        found_reflection = True
        fixed = False
        numToCheck = min(x + 1, m - x - 1)

        for colDiff in range(numToCheck):
            
            lCol = x - colDiff
            rCol = x + colDiff + 1
            for y in range(n):
                if grid[y][lCol] != grid[y][rCol]:
                    if not fixed:
                        fixed = True
                    else:
                        found_reflection = False
                        break
            if not found_reflection: break
        if found_reflection:
            return (0, x + 1)

    # try to find a horizontal reflection
    for y in range(0, n-1):
        # ignore this potential reflection this was the previous solution for part 1
        if prevSol == (y+1, 0):
            continue

        found_reflection = True
        fixed = False
        numToCheck = min(y + 1, n - y - 1)

        for rowDiff in range(numToCheck):
            lRow = y - rowDiff
            rRow = y + rowDiff + 1
            for x in range(m):
                if grid[lRow][x] != grid[rRow][x]:
                    if not fixed:
                        fixed = True
                    else:
                        found_reflection = False
                        break
            if not found_reflection: break

        if found_reflection:
            return (y + 1, 0)

    # x reflection then y reflection
    return 0, 0 

def day13_part1(input):
    input = [x.split('\n') for x in input.split('\n\n')]
    vals  = [findReflection(x) for x in input]

    return sum([100 * a + b for (a, b)  in vals])

def day13_part2(input):
    input = [x.split('\n') for x in input.split('\n\n')]
    vals  = [findSmudgedReflection(x) for x in input]

    return sum([100 * a + b for (a, b)  in vals])

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day13_part1(example_input) == 405
    print(day13_part1(test_input))

    assert day13_part2(example_input) == 400
    print(day13_part2(test_input))