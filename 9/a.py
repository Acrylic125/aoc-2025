
def parse_coords(s):
    x, y = s.split(",")
    return (int(x), int(y))

# with open("9/test.txt", "r") as f:
with open("9/input.txt", "r") as f:
    lines = f.readlines()
    
    coords = list(map(parse_coords, lines))

    pairs = []
    largest = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            area = (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)
            largest = max(area, largest)

    print(largest)
