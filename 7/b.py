import re

# with open("6/test.txt", "r") as f:
with open("6/input.txt", "r") as f:
    lines = f.readlines()

    _operands = list(map(lambda v: v.replace('\n', ''), lines[:-1]))
    _operators = lines[-1].replace('\n', '')

    nums = []
    size = 0
    for c in _operators:
        if c != ' ':
            if size != 0:
                nums.append(size)
            size = 1
        else:
            size += 1
    # size -= 1
    nums.append(size)

    # print(nums)
    # *   +   *   +  -
    # 012345678901234

    # Pad chars
    # for i in range(len(_operands)):
    #     _operands[i] = _operands[i].ljust(len(_operators), ' ')

    print(_operands)

    results = []
    for _j, num in enumerate(nums):
        rows = len(_operands)
        from_j = sum(nums[:_j])
        to_j = from_j+num
        
        operator = _operators[from_j]
        tally = 0
        for j in range(from_j, to_j):
            val = 0
            for i in range(rows):
                if _operands[i][j] == ' ':
                    # print(f"FUUUU {i} {j}")
                    continue
                val *= 10
                val += int(_operands[i][j])
            if val == 0:
                break
            print(val, operator, tally)
            # print(val)
            if j == from_j:
                tally = val 
            elif operator == "+":
                tally += val 
            elif operator == "*":
                tally *= val 
        results.append(tally)
        print(results)

    print(sum(results))



