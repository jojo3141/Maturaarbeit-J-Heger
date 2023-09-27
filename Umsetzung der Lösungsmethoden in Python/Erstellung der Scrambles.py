from Rubiks_Cube import *
with open("scrambles_list.txt", "w") as file:
    for i in range(10000):
        file.write(str(scramble(30))+"\n")