
with open("3/input.txt", "r") as f:
# with open("3/test.txt", "r") as f:
    lines = f.readlines()
    tally = 0
    for l in lines:
        number_of_1s_to_remove = max(len(l) - 12, 0)
        l = l.replace("\n", "")
        prev_index = 0
        s = ""
        for i in range(11, -1, -1):
            print(f"  {prev_index} {i}")
            highest_j_index = -1
            for j in range(prev_index, len(l) - i):
                if highest_j_index == -1 or int(l[j]) > int(l[highest_j_index]):
                    highest_j_index = j
            if highest_j_index >= 0:
                prev_index = highest_j_index + 1
                s = s + l[highest_j_index]

        print(s)
        tally += int(s)
        print(l, s)
    print(tally)
                

        

