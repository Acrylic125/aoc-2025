
# with open("5/test.txt", "r") as f:
with open("5/input.txt", "r") as f:
    fresh_ranges = []

    lines = f.readlines()
    for l in lines:
        l = l.replace("\n", "")
        if l == "":
            break
        _min, _max = l.split("-")
        _min, _max = int(_min), int(_max)
        if _max < _min:
            raise ValueError("max smaller than min")
        fresh_ranges.append((_min, _max))

    fresh_ranges.sort(key=lambda a: a[0])
    last_highest = fresh_ranges[0][0] - 1
    tally = 0
    for (_min, _max) in fresh_ranges:
        modified_min = max(_min, last_highest + 1)
        if last_highest > _max:
            continue
        delta = _max - modified_min + 1
        print(modified_min, _max)
        tally += delta
        last_highest = _max
    print(tally)
     
        

