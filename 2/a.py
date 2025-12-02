import re


def has_pattern(s):
    return re.match(r"^(.+)\1$", s)
    # return re.match(r"^(.+)(\1)+$", s)
    # return re.match(r"^(.+?)(?:\\1)+$", s)
    # cur_pattern = ""
    # for c in s:
    #     if cur_pattern

# print(has_pattern("121212"))
# print(has_pattern("12121"))

# with open("2/test.txt", "r") as f:
with open("2/input.txt", "r") as f:
    line = f.readline()
    line = line.replace("\n", "")
    all_ranges = line.split(",")
    invalid_ids_sum = 0
    for ranges in all_ranges:
        split = ranges.split("-")
        if len(split) != 2:
            continue
        _l, _h = split
        l = int(_l)
        h = int(_h)
        # print(h-l)
        for i in range(l, h+1):
            if has_pattern(f"{i}"):
                print(f"{l} {h+1}: {i}")
                invalid_ids_sum += i
    print(invalid_ids_sum)
                

        

