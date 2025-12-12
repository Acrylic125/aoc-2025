from typing import List

def rotate_pattern(pattern: List[str]) -> List[str]:
    """Rotate 90° clockwise."""
    if not pattern or not pattern[0]:
        return []
    rows = len(pattern)
    cols = len(pattern[0])
    return [
        "".join(pattern[rows - 1 - r][c] for r in range(rows))
        for c in range(cols)
    ]

def flip_horz(pattern: List[str]) -> List[str]:
    """Flip horizontally (mirror left-right)."""
    return [row[::-1] for row in pattern]

def serialize_pattern(pattern: List[str]) -> str:
    return "+".join(pattern)

def replace_char_at_pos(s: str, pos: int, new: str) -> str:
    return s[:pos] + new + s[pos+1:]

def deep_copy_mapping(mapping: List[str]) -> List[str]:
    return [row for row in mapping]

def verify_fit(selections: List[int], patterns: List[List[str]], mapping: List[str]) -> bool:
    H = len(mapping)
    W = len(mapping[0])

    area = W * H 

    tally_required_area = 0
    for selection_i in range(len(selections)):
        pattern = patterns[selection_i]
        pattern_area = 0
        for line in pattern:
            for c in line:
                if c == "#":
                    pattern_area += 1
        print(f"  {pattern_area} {selections[selection_i]} {pattern}")
        tally_required_area += (pattern_area * selections[selection_i])
    
    print(tally_required_area, area)
    return tally_required_area <= area
    # if tally_required_area > area:
    #     return False

    # find next pattern type that still has pieces leftover
    next_selection = -1
    for idx in range(len(selections)):
        if selections[idx] > 0:
            next_selection = idx
            break

    # if all zero, we succeeded
    if next_selection == -1:
        return True

    pattern = patterns[next_selection]

    H = len(mapping)
    W = len(mapping[0])

    # precompute all 8 orientations (4 rotations × flip/nonflip)
    orientations = {}
    cur = pattern
    for _ in range(4):
        for flipped in (False, True):
            p = flip_horz(cur) if flipped else cur
            orientations[serialize_pattern(p)] = p
        cur = rotate_pattern(cur)
    orientations = list(orientations.values())

    # try placing pattern at every mapping position
    for anchor_i in range(H):
        for anchor_j in range(W):

            for pat in orientations:
                ph = len(pat)
                pw = len(pat[0])

                # check fit boundaries
                if anchor_i + ph > H or anchor_j + pw > W:
                    continue

                # verify we can place
                okay = True
                for pi in range(ph):
                    for pj in range(pw):
                        if pat[pi][pj] == "#":
                            if mapping[anchor_i + pi][anchor_j + pj] != ".":
                                okay = False
                                break
                    if not okay:
                        break

                if not okay:
                    continue

                # place piece
                new_mapping = deep_copy_mapping(mapping)
                for pi in range(ph):
                    for pj in range(pw):
                        if pat[pi][pj] == "#":
                            row = new_mapping[anchor_i + pi]
                            new_mapping[anchor_i + pi] = replace_char_at_pos(row, anchor_j + pj, "#")

                new_selections = selections[:]
                new_selections[next_selection] -= 1

                if verify_fit(new_selections, patterns, new_mapping):
                    return True

    return False

# with open("12/test.txt", "r") as f:
with open("12/input.txt", "r") as f:
    lines = f.read().strip()
    groups = lines.split("\n\n")

    # parse patterns
    patterns = []
    for group in groups[:-1]:
        block = group.split("\n")
        patterns.append(block[1:])  # drop the "shape X" line

    # parse regions
    regions = []
    for line in groups[-1].split("\n"):
        if not line.strip():
            continue
        dim, sel = line.split(": ")
        w, h = map(int, dim.split("x"))
        selections = list(map(int, sel.split(" ")))
        regions.append({
            "width": w,
            "height": h,
            "selections": selections
        })

    tally = 0
    for region in regions:
        w = region["width"]
        h = region["height"]
        selections = region["selections"]
        mapping = ["." * w for _ in range(h)]
        if verify_fit(selections, patterns, mapping):
            print(region)
            tally += 1
        else:
            print(f"Failed {region}")

    print(tally)


# from typing import List
#
# def rotate_pattern(pattern: List[str]) -> List[str]:
#     if not pattern or not pattern[0]:
#         return []
#         
#     return [
#         "".join(reversed(chars)) 
#         for chars in zip(*pattern)
#     ]
#
# def replace_char_at_pos(s, pos, new_char):
#     # Ensure the position is valid
#     if pos < 0 or pos >= len(s):
#         return "Error: Position out of bounds"
#     
#     # Create a new string using slicing and concatenation
#     new_s = s[:pos] + new_char + s[pos+1:]
#     return new_s
#
# def flip_horz(pattern: List[str]) -> List[str]:
#     new_pattern = []
#     for line in pattern:
#         n_line = []
#         for i in range(len(pattern)):
#             n_line.append(line[len(pattern)-1-i])
#         new_pattern.append("".join(n_line))
#     return new_pattern
#
# def serialize_pattern(pattern: List[str]) -> str:
#     return "+".join(pattern)
#
# def verify_fit(selections: List[int], patterns: List[List[str]], mapping: List[str]):
#     next_selection = -1
#     for si in range(len(selections)):
#         if selections[si] > 0:
#             next_selection = si
#     # We are done, we found a fit.
#     if next_selection == -1:
#         return True
#
#     for i in range(len(mapping)):
#         for j in range(len(mapping[0])):
#             pattern = patterns[next_selection]
#
#             # Hash the patterns to avoid redundancies.
#             patterns_to_try = {}
#             # We try all 4 rotations.
#             for _ in range(4):
#                 # We try flipped and non flip
#                 for m in range(2):
#                     _pattern = pattern 
#                     if m == 1:
#                         _pattern = flip_horz(pattern)
#
#                     # Now we check for fit.
#                     can_fit = True
#                     for pi in range(len(_pattern)):
#                         for pj in range(len(_pattern[0])):
#                             if _pattern[pi][pj] == ".":
#                                 continue
#                             piece_i = pi + i
#                             piece_j = pj + j
#                             if piece_i < 0 or piece_i >= len(mapping):
#                                 can_fit = False
#                                 break
#                             if piece_j < 0 or piece_j >= len(mapping[0]):
#                                 can_fit = False
#                                 break
#                             if mapping[piece_i][piece_j] != ".":
#                                 can_fit = False 
#                                 break
#                         if not can_fit:
#                             break
#
#                     if can_fit:
#                         patterns_to_try[serialize_pattern(_pattern)] = _pattern
#
#                 # Process next pattern with rotation.
#                 pattern = rotate_pattern(pattern)
#
#             for _pattern_key in patterns_to_try:
#                 _pattern = patterns_to_try[_pattern_key]
#                 new_mapping = []
#                 for i in range(len(mapping)):
#                     new_mapping.append(mapping[i])
#                 for pi in range(len(_pattern)):
#                     for pj in range(len(_pattern[0])):
#                         if _pattern[pi][pj] == ".":
#                             continue
#                         piece_i = pi + i
#                         piece_j = pj + j
#                         print(len(new_mapping))
#                         print(piece_i)
#                         print(piece_j, piece_j, len(new_mapping[piece_i]))
#                         new_mapping[piece_i] = replace_char_at_pos(new_mapping[piece_i], piece_j, "#")
#                 new_selections = [*selections]
#                 new_selections[next_selection] -= 1
#                 res = verify_fit(new_selections, patterns, new_mapping)
#                 if res == True:
#                     return True
#     return False
#
#
# with open("12/test.txt", "r") as f:
# # with open("12/input.txt", "r") as f:
#     lines = f.read()
#
#     groups = lines.split("\n\n")
#
#     patterns = []
#     for group in groups[:len(groups)-1]:
#         pattern = group.split('\n')
#         patterns.append(pattern[1:])
#
#     regions = []
#     for group in groups[len(groups)-1].split("\n"):
#         if group == "":
#             continue
#         dim, selections = group.split(": ")
#         width, height = dim.split("x")
#         selections = selections.split(" ")
#         regions.append({
#             "width": int(width),
#             "height": int(height),
#             "selections": list(map(int, selections))
#         })
#
#     tally = 0
#     for region in regions:
#         width = region["width"]
#         height = region["height"]
#         selections = region['selections']
#         mapping = [("." * width) for _ in range(height)]
#         if verify_fit(selections, patterns, mapping):
#             tally += 1
#     print(tally)
#
#     # print(patterns, regions)
#
