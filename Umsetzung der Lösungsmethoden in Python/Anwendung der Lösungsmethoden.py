
from Rubiks_Cube import *

with open("solves_data/scrambles_list.txt", "w") as file:
    for i in range(10000):
        file.write(str(scramble(30))+"\n")

with open("solves_data/scrambles_list.txt", "r") as file:
    lines = file.readlines()

all_scrambles = []
for line in lines:
    all_scrambles.append(eval(line.strip()))


with open("CFOP_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveCFOP(scr, False)))+"\n")


with open("CFCE_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveCFCE(scr, False)))+"\n")


with open("LBL_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveLBL(scr, False)))+"\n")

with open("ROUX_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveROUX(scr, False)))+"\n")

