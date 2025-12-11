from typing import Dict





def replace_char_at_index_slicing(original_string, index, new_char):
    if not (0 <= index < len(original_string)):
        raise IndexError("Index out of bounds")
    return original_string[:index] + new_char + original_string[index + 1:]

def toggle_indicators(indicator_lights, schematic):
    for toggle_i in schematic:
        if indicator_lights[toggle_i] == ".":
            indicator_lights = replace_char_at_index_slicing(indicator_lights, toggle_i, "#")
        else:
            indicator_lights = replace_char_at_index_slicing(indicator_lights, toggle_i, ".")
    return indicator_lights

with open("10/test.txt", "r") as f:
# with open("10/input.txt", "r") as f:
    lines = f.readlines()

    s = 0
    for line in lines:
        groups = line.split(" ")
        indicator_lights = groups[0]
        _schematics = groups[1:len(groups)-1]
        joltage = groups[len(groups)-1]

        indicator_lights = indicator_lights.replace("[", "")
        indicator_lights = indicator_lights.replace("]", "")

        schematics = []
        for schematic in _schematics:
            schematic = schematic.replace("(", "")
            schematic = schematic.replace(")", "")
            schematic = list(map(int, schematic.split(",")))
            schematics.append(schematic)

        joltage = joltage.replace("{", "")
        joltage = joltage.replace("}", "")
        joltage = list(map(int, joltage.split(",")))
        print(joltage)

        _all_off = "." * len(indicator_lights)
        _all_joltage_0 = ",".join(["0"] * len(joltage))
        main_key = f"{_all_off}-{_all_joltage_0}"
        min_paths: Dict[str, int] = {
            main_key: 0
        }
        to_explore = [main_key]

        while len(to_explore) > 0:
            cur = to_explore.pop(0)
            cur_weight = min_paths[cur]
            cur_indicator_lights, cur_joltage = cur.split("-")
            cur_joltage = list(map(int, cur_joltage.split(",")))
            if cur_indicator_lights == indicator_lights:
                is_all_satisfied = True
                for i in range(len(joltage)):
                    if cur_joltage[i] < joltage[i]:
                        is_all_satisfied = False
                if is_all_satisfied:
                    print(f"Found {cur_weight}")
                    s += cur_weight
                    break
            for schematic in schematics:
                toggled = toggle_indicators(cur_indicator_lights, schematic)
                # Check if its already explored. If so, ignore.
                if min_paths.get(toggled) != None:
                    continue
                new_joltage = list(map(lambda v: f"{v + 1}", cur_joltage))
                joltage_key = ",".join(new_joltage)
                key = f"{toggled}-{joltage_key}"
                min_paths[key] = cur_weight + 1
                to_explore.append(key)
        
    print(s)

# from typing import Dict, List, Tuple
#
#
#
#
#
# def replace_char_at_index_slicing(original_string, index, new_char):
#     if not (0 <= index < len(original_string)):
#         raise IndexError("Index out of bounds")
#     return original_string[:index] + new_char + original_string[index + 1:]
#
# def toggle_indicators(indicator_lights, schematic):
#     for toggle_i in schematic:
#         if indicator_lights[toggle_i] == ".":
#             indicator_lights = replace_char_at_index_slicing(indicator_lights, toggle_i, "#")
#         else:
#             indicator_lights = replace_char_at_index_slicing(indicator_lights, toggle_i, ".")
#     return indicator_lights
#
# with open("10/test.txt", "r") as f:
# # with open("10/input.txt", "r") as f:
#     lines = f.readlines()
#
#     s = 0
#     for line in lines:
#         groups = line.split(" ")
#         indicator_lights = groups[0]
#         _schematics = groups[1:len(groups)-1]
#         joltage = groups[len(groups)-1]
#
#         indicator_lights = indicator_lights.replace("[", "")
#         indicator_lights = indicator_lights.replace("]", "")
#
#         schematics = []
#         for schematic in _schematics:
#             schematic = schematic.replace("(", "")
#             schematic = schematic.replace(")", "")
#             schematic = list(map(int, schematic.split(",")))
#             schematics.append(schematic)
#
#         joltage = joltage.replace("{", "")
#         joltage = joltage.replace("}", "")
#         joltage = list(map(int, joltage.split(",")))
#
#         _all_off = "." * len(indicator_lights)
#         _all_joltage_0 = [0] * len(joltage)
#         min_paths: Dict[str, List[Tuple[int, List[int]]]] = {
#             _all_off: [
#                 (0, _all_joltage_0)
#             ]
#         }
#         to_explore = [_all_off]
#
#         while len(to_explore) > 0:
#             cur = to_explore.pop(0)
#             paths = min_paths[cur]
#             if cur == indicator_lights:
#                 should_break = False
#                 for weight, joltages in paths:
#                     is_all_satisfied = True
#                     for i in range(len(joltage)):
#                         if joltages[i] >= joltage[i]:
#                             is_all_satisfied = False
#                     if is_all_satisfied:
#                         print(f"Found {weight}")
#                         s += weight
#                         should_break = True
#                         break
#                 if should_break:
#                     break
#             for schematic in schematics:
#                 toggled = toggle_indicators(cur, schematic)
#                 for weight, joltages in paths:
#                     if min_paths.get(toggled) == None:
#                         new_joltage = list(map(lambda v: v + 1, joltages))
#                         min_paths[toggled].append((weight + 1, new_joltage))
#                         to_explore.append(toggled)
#                         continue
#
#                     # Check if its already explored. If so, ignore.
#                     # if min_paths.get(toggled) != None:
#                     #     continue
#                     # new_joltage = list(map(lambda v: f"{v + 1}", cur_joltage))
#                     # joltage_key = ",".join(new_joltage)
#                     # key = f"{toggled}-{joltage_key}"
#                     # min_paths[key] = cur_weight + 1
#                     # to_explore.append(key)
#         
#     print(s)
#
#
