from typing import Dict

# with open("11/test-2.txt", "r") as f:
with open("11/input.txt", "r") as f:
    lines = f.readlines()

    paths = {}

    for line in lines:
        split = line.split(": ")
        key = split[0]
        next_nodes = split[1].replace('\n', '').split(" ")
        paths[key] = next_nodes

    def count_paths(cur, memo, visited_dac, visited_fft):
        key = f"{cur} {visited_dac} {visited_fft}"
        if memo.get(key) != None:
            return memo[key]
        if cur == 'out':
            # print(cur, visited_dac, visited_fft)
            return 1 if visited_fft and visited_dac else 0
        if cur == 'dac':
            visited_dac = True
        if cur == 'fft':
            visited_fft = True
        # print(cur, visited_dac, visited_fft)
        tally = 0
        for p in paths[cur]:
            tally += count_paths(p, memo, visited_dac, visited_fft)
        # return tally
        memo[key] = tally
        return memo[key]
    
    print(count_paths("svr", {}, False, False))

