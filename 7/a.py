import re

# with open("7/test.txt", "r") as f:
with open("7/input.txt", "r") as f:
    lines = f.readlines()

    grid = [] 
    for line in lines:
        s = line.replace('\n', '')
        grid.append(s)

    S = (0,0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                S = (i, j)

    split_at_hashes = set()
    splitters = set()
    traversed = set()
    beams = [(S[0], S[1])]
    while len(beams) > 0:
        (i, j) = beams.pop(0)
        traversed.add(f"{i} {j}")
        if i < 0 or i >= len(grid):
            continue
        if j < 0 or j >= len(grid[0]):
            continue
        if grid[i][j] == '^':
            dirs = [[0, -1], [0, 1]]
            splitters.add(f"{i} {j}")
            for (dx, dy) in dirs:
                hash = f"{i + dx} {j + dy}"
                if hash in split_at_hashes:
                    continue
                split_at_hashes.add(hash)
                beams.append((i + dx, j + dy))
        else:
            beams.append((i + 1, j))

    print(len(splitters))
    # print(len(split_at_hashes))
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == '^':
    #             print('^', end='')
    #         elif f"{i} {j}" in traversed:
    #             print('|', end='')
    #         else:
    #             print(grid[i][j], end='')
    #     print('\n', end='')
    #
    #
