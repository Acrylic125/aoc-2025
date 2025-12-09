def parse_coords(s):
    x, y = s.split(",")
    return (int(x), int(y))

def calc_area(coords):
    v1, v2 = coords
    area = (abs(v1[0] - v2[0]) + 1) * (abs(v1[1] - v2[1]) + 1)
    return area

def point_on_segment(p, seg_start, seg_end):
    x, y = p
    x1, y1 = seg_start
    x2, y2 = seg_end
    
    # Check if point is within bounding box
    if not (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)):
        return False
    
    # Check collinearity using cross product
    cross = (y - y1) * (x2 - x1) - (x - x1) * (y2 - y1)
    return cross == 0

def point_in_polygon(p, edges):
    x, y = p
    
    # Check if point is on any edge or vertex
    for edge in edges:
        if point_on_segment(p, edge[0], edge[1]):
            return True
    
    # Ray casting algorithm for interior points
    inside = False
    for edge in edges:
        x1, y1 = edge[0]
        x2, y2 = edge[1]
        
        # Check if ray crosses edge
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    
    return inside

def rectangle_in_polygon(rect, edges):
    v1, v2 = rect
    lo_x = min(v1[0], v2[0])
    lo_y = min(v1[1], v2[1])
    hi_x = max(v1[0], v2[0])
    hi_y = max(v1[1], v2[1])

    # Four corners of the rectangle
    corners = [
        (lo_x, lo_y),
        (lo_x, hi_y),
        (hi_x, lo_y),
        (hi_x, hi_y)
    ]

    # All corners must be inside or on the polygon
    # Quick check
    for corner in corners:
        if not point_in_polygon(corner, edges):
            return False
    
    # print(f"{hi_x - lo_x + 1} {hi_y - lo_y + 1} {len(edges)}")
    # Sampling check, no guarantee
    for x in range(lo_x, hi_x+1, 20):
        if not point_in_polygon((x, lo_y), edges):
            return False
        if not point_in_polygon((x, hi_y), edges):
            return False

    for y in range(lo_y, hi_y+1, 20):
        if not point_in_polygon((lo_x, y), edges):
            return False
        if not point_in_polygon((lo_y, y), edges):
            return False
    # print("Done")


    # for x in range(lo_x, hi_x+1):
    #     for y in range(lo_y, hi_y+1):
    #         if not point_in_polygon((x, y), edges):
    #             return False
    
    return True

# with open("9/test.txt", "r") as f:
with open("9/input.txt", "r") as f:
    lines = f.readlines()
    
    coords = list(map(parse_coords, lines))
    edges = []
    for i in range(len(coords)):
        edges.append((coords[i], coords[(i + 1) % len(coords)]))
    
    # Generate all possible rectangles from pairs of polygon vertices
    rects = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            rects.append((coords[i], coords[j]))
    
    rects.sort(key=calc_area)
    
    # Check from largest to smallest
    print(len(rects))
    # 102620
    while len(rects) > 90_000:
    # while len(rects) > 115080:
        rect = rects.pop()

    while len(rects) > 0:
        rect = rects.pop()
        area = calc_area(rect)

        if len(rects) % 20 == 0:
            print(f"Left: {len(rects)}")
        
        # Check if this rectangle fits in the polygon
        if rectangle_in_polygon(rect, edges):
            best_area = area
            best_rect = rect
            v1, v2 = rect
            lo_x = min(v1[0], v2[0])
            lo_y = min(v1[1], v2[1])
            hi_x = max(v1[0], v2[0])
            hi_y = max(v1[1], v2[1])
            print(f"Found rectangle: ({lo_x}, {lo_y}) to ({hi_x}, {hi_y}), area: {area}")
            break
