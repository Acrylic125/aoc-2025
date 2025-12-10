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

# with open("10/test.txt", "r") as f:
with open("10/input.txt", "r") as f:
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

        _all_off = "." * len(indicator_lights)
        min_paths: Dict[str, int] = {
            _all_off: 0
        }
        to_explore = [_all_off]

        while len(to_explore) > 0:
            cur = to_explore.pop(0)
            cur_weight = min_paths[cur]
            if cur == indicator_lights:
                print(f"Found {cur_weight}")
                s += cur_weight
                break
            for schematic in schematics:
                toggled = toggle_indicators(cur, schematic)
                # Check if its already explored. If so, ignore.
                if min_paths.get(toggled) != None:
                    continue
                min_paths[toggled] = cur_weight + 1
                to_explore.append(toggled)
        
    print(s)

