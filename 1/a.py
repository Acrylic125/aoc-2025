


dial = 50
full_dial = 100
num_of_0 = 0
with open("1/input.txt", "r") as f:
# with open("1/test.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        if l.startswith("L"):
            rotation = int(l.replace("L", ''))
            dial = (dial - rotation) % full_dial
        if l.startswith("R"):
            rotation = int(l.replace("R", ''))
            dial = (dial + rotation) % full_dial
        if dial == 0:
            num_of_0 += 1

print(num_of_0)


