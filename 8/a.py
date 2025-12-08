
def parse_coords(s):
    x, y, z = s.split(",")
    return (int(x), int(y), int(z))

def is_same_coords(v1, v2):
    return v1[0] == v2[0] and v1[1] == v2[1] and v1[2] == v2[2]

def calc_dist(v1, v2):
    d = 0
    for i in range(3):
        _d = v1[i] - v2[i]
        d += (_d * _d)
    return d

# with open("8/test.txt", "r") as f:
with open("8/input.txt", "r") as f:
    lines = f.readlines()
    
    coords = list(map(parse_coords, lines))

    edges = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            edges.append((i, j))
    
    # Sort edges 
    edges.sort(key=lambda v: calc_dist(coords[v[0]], coords[v[1]]))

    circuits = [(i, False) for i in range(len(coords))]

    c = 0
    N = 1000
    while len(edges) > 0:
        all_connected = True 
        for circuit in circuits:
            if not circuit[1]:
                all_connected = False
                break
        if all_connected:
            break
        if c >= N:
            break

        left, right = edges.pop(0)
        c += 1

        # Find left parent
        left_parent = circuits[left][0]
        while left_parent != circuits[left_parent][0]:
            left_parent = circuits[left_parent][0]

        # Find right parent
        right_parent = circuits[right][0]
        while right_parent != circuits[right_parent][0]:
            right_parent = circuits[right_parent][0]

        # Left connects to right
        circuits[left_parent] = (right_parent, True)

    circuit_sizes = {}
    for i in range(len(circuits)):
        parent, _ = circuits[i]
        while parent != circuits[parent][0]:
            parent = circuits[parent][0]
        if circuit_sizes.get(f"{parent}") == None:
            circuit_sizes[f"{parent}"] = 0
        circuit_sizes[f"{parent}"] += 1
    
    all_vs = []
    for k in circuit_sizes:
        v = circuit_sizes[k]
        if v > 1:
            all_vs.append(v)
    all_vs.sort(reverse=True)
    print(all_vs[0] * all_vs[1] * all_vs[2])

    # for v1, v2 in edges:
    #     print(v1, v2)
