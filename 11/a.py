from typing import Dict


# with open("11/test.txt", "r") as f:
with open("11/input.txt", "r") as f:
    lines = f.readlines()

    paths = {}

    for line in lines:
        split = line.split(": ")
        key = split[0]
        next_nodes = split[1].replace('\n', '').split(" ")
        paths[key] = next_nodes

    def count_paths(cur, memo):
        if memo.get(cur) != None:
            return memo[cur]
        if cur == 'out':
            return 1
        tally = 0
        for p in paths[cur]:
            tally += count_paths(p, memo)
        memo[cur] = tally
        return memo[cur]
    
    print(count_paths("you", {}))

