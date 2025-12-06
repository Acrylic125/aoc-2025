import re

# with open("6/test.txt", "r") as f:
with open("6/input.txt", "r") as f:
    lines = f.readlines()

    _operands = lines[:-1]
    _operators = lines[-1]

    nums = []
    for o in _operands:
        o1 = re.sub(r"( )+", ' ', o.strip().replace('\n', '')).split(' ')
        print(o1)
        nums.append(list(map(lambda v: int(v), o1)))

    ops = re.sub(r"( )+", ' ', _operators.strip().replace('\n', ''))
    ops = ops.split(' ')

    results = [0] * (len(ops))
    for i in range(len(nums)):
        for j in range(len(ops)):
            n = nums[i][j]

            if i == 0:
                results[j] = n
            elif ops[j] == '+':
                results[j] += n
            elif ops[j] == '*':
                results[j] *= n
        print(results)

    print(results)
    print(sum(results))
