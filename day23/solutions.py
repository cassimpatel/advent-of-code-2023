def parse_input(input):
    grid = [[y for y in x] for x in input.split('\n')]
    return grid

def get_neighs(grid, cur):
    neighs = {'<':(0, -1), '>':(0, 1), '^':(-1, 0), 'v':(1, 0)}
    n = len(grid)
    m = len(grid[0])
    y, x = cur

    if grid[y][x] in '<>^v':
        dy, dx = neighs[grid[y][x]]
        return [((y + dy, x + dx), 1)]

    res = []
    for dy, dx in neighs.values():
        ny, nx = y + dy, x + dx
        if not 0 <= ny < n: continue
        if not 0 <= nx < m: continue
        if grid[ny][nx] == '#': continue
        res.append(((ny, nx), 1))
    
    return res

def bfs_longest_path(graph, start, end, neighbour_func=get_neighs):
    cost = {}

    queue = [(start, set())]
    cost[start] = 0
    while queue:
        (cur, path) = queue.pop(0)

        if cur == end:
            continue
        
        for (nxt, cst) in neighbour_func(graph, cur):
            if nxt in path: continue
            new_c = cost[cur] + cst
            if nxt not in cost or new_c > cost[nxt]:
                cost[nxt] = new_c
                new_path = path.copy()
                new_path.add(nxt)
                queue.append((nxt, new_path))
    
    res = cost[end]
    return res

def day23_part1(input):
    grid = parse_input(input)
    n = len(grid)
    m = len(grid[0])
    
    return bfs_longest_path(grid, (0, 1), (n-1, m-2))

def next_intersection(grid, vis, start):
    path_len = 0

    cur = start
    while True:
        vis.add(cur)

        neighs = get_neighs(grid, cur)
        if len(neighs) == 1:
            # we've backed into a dead end
            return (cur, path_len)

        neighs = [node for (node,_) in neighs if node not in vis]
        if len(neighs) == 0:
            # we're one away from an intersection that we've already visited
            intersec = [node for (node, _) in get_neighs(grid, cur) if node in vis and len(get_neighs(grid, node)) > 1][0]
            return (intersec, path_len + 1)
        if len(neighs) > 1:
            # we've landed on an non-visited intersection
            return (cur, path_len)

        cur = neighs.pop(0)
        path_len += 1

def build_smaller_graph(grid, start):
    visited = set()
    graph = {}

    def dfs(node):
        # initialise graph node for this intersection, mark as visited
        nonlocal graph
        if node not in graph:
            graph[node] = {}
        visited.add(node)

        # for each neighbour, follow through to the next intersection, update graph, recur
        for (nxt, _) in get_neighs(grid, node):
            if nxt in visited: continue
            next_int, path_len = next_intersection(grid, visited, nxt)
            graph[node][next_int] = path_len + 1
            # print(f'gone from {node} to {next_int} with cost {path_len + 1}')
            dfs(next_int)
    dfs(start)

    # add all reversed edges to graph
    for node in graph:
        for nxt in graph[node]:
            graph[nxt][node] = graph[node][nxt]

    return graph

def day23_part2(input):
    # replace forced directions
    for val in '<>^v':
        input = input.replace(val, '.')
    grid = parse_input(input)

    # calculate start and end, simpler graph
    n = len(grid)
    m = len(grid[0])
    strt = (0, 1)
    end  = (n-1, m-2)
    grph = build_smaller_graph(grid, (0, 1))

    # run DFS to find longest path
    seen = set()
    res = 0
    def dfs(node, dist):
        nonlocal res
        if node in seen: return
        seen.add(node)
        if node == end:
            res = max(res, dist)
        for (nxt, path_len) in grph[node].items():
            dfs(nxt, dist + path_len)
        seen.discard(node)
    dfs(strt, 0)
        
    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day23_part1(example_input) == 94
    print(day23_part1(test_input))

    assert day23_part2(example_input) == 154
    print(day23_part2(test_input))