
# with open("5/test.txt", "r") as f:
with open("5/input.txt", "r") as f:
    fresh_ranges = []
    fresh = []

    lines = f.readlines()
    has_passed_ranges = False 
    for l in lines:
        l = l.replace("\n", "")
        if not has_passed_ranges:
            if l == "":
                has_passed_ranges = True 
                continue
            print(l)
            _min, _max = l.split("-")
            min, max = int(_min), int(_max)
            fresh_ranges.append((min, max))
            continue
        id = int(l)
        is_within_range = False
        for (min, max) in fresh_ranges:
            if id >= min and id <= max:
                is_within_range = True 
                break
        if is_within_range:
            fresh.append(id)

    print(len(fresh))
        
        

