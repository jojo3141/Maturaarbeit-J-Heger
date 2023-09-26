"""#with open("solves_data/scrambles_list.txt", "w") as file:
    for i in range(10000):
        file.write(str(scramble(30))+"\n")


with open("solves_data/scrambles_list.txt", "r") as file:
    lines = file.readlines()

all_scrambles = []
for line in lines:
    all_scrambles.append(eval(line.strip()))


with open("solves_data/CFOP_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveCFOP(scr, False)))+"\n")
"""