
# with open("4/test.txt", "r") as f:
with open("4/input.txt", "r") as f:
    lines = f.readlines()

    grid = []
    marked = []
    for l in lines:
        grid.append(l)
        marked.append([0] * len(l))
    print(f"{len(grid)} {len(grid[0])}")

    dirs = [
            [1, 0],
            [0, 1],
            [1, 1],
            [1, -1],
            [-1, 0],
            [0, -1],
            [-1, -1],
            [-1, 1],
    ]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '@':
                continue
            # number_of_rolls = 0
            rolls = []
            has_forklift = False
            for (dx, dy) in dirs:
                nx = i + dx
                ny = j + dy
                if nx < 0 or nx >= len(grid):
                    continue
                if ny < 0 or ny >= len(grid[0]):
                    continue
                if grid[nx][ny] == '.':
                    has_forklift = True
                if grid[nx][ny] == '@':
                    rolls.append((nx, ny))
            # print(f"{i} {j} {rolls}")
            if len(rolls) < 4 and has_forklift:
                marked[i][j] = 1
                # for (nx, ny) in rolls: 
                #     marked[nx][ny] = 1


    # for (dx, dy) in dirs:
    #     marked[0 + dx][1 + dy] = 1

    tally = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tally += marked[i][j]
            # if marked[i][j] == 1:
            #     print('x', end='')
            # else:
            #     print(grid[i][j], end='')
    print(tally)

