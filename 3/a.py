
# with open("3/test.txt", "r") as f:
with open("3/input.txt", "r") as f:
    lines = f.readlines()
    tally = 0
    for l in lines:
        highest_joltage = 0
        for i in range(0, len(l)):
            for j in range(i+1, len(l)):
                joltage = int(l[i] + l[j])
                highest_joltage = max(highest_joltage, joltage)
        print(l, highest_joltage)
        tally += highest_joltage
    print(tally)
                

        

