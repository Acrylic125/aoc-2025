from typing import Dict
from z3 import *


# with open("10/test.txt", "r") as f:
with open("10/input.txt", "r") as f:
    lines = f.readlines()

    tally = 0
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

        # s = Solver()
        s = Optimize()
        X = Ints([f"x{i}" for i in range(len(schematics))])
        # objective = x + y
        s.minimize(Sum(X))
        
        for x in X:
            s.add(x >= 0)

        for joltage_index in range(len(joltage)):
            j = joltage[joltage_index]
            equation = []
            for schematic_index in range(len(schematics)):
                schematic = schematics[schematic_index]
                if joltage_index in schematic:
                    equation.append(X[schematic_index])
        
                # for schem in schematic:
                #     if schem == joltage_index: 
                #     equation.append(X[schem])
            s.add(Sum(equation) == j)
        if s.check() == sat:
            model = s.model()
            for x in X:
                print(f"  {x} = {model[x]}")
                tally += model[x].as_long()
            print(f"{X}")
                # print(model[x])
                # s += model[x].as_long()
        else:
            print("Not satisfiable.")
        
    print(tally)

