import networkx as nx

def parse_input(input):
    input = [x.split() for x in input.replace(':', '').split('\n')]
    G = nx.Graph()
            
    for part in input:
        lab, others = part[0], part[1:]
        for nxt in others:
            G.add_edge(lab, nxt)

    return G

def day25_part1(input):
    G = parse_input(input)

    # get minimum set of edges to disconnect the graph
    cuts = nx.minimum_edge_cut(G)
    G.remove_edges_from(cuts)

    # get connected groups from remaining graph, sizes of groups
    groups = list(nx.connected_components(G))
    group_sizes = [len(x) for x in groups]

    return group_sizes[0] * group_sizes[1]

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day25_part1(example_input) == 54
    print(day25_part1(test_input))