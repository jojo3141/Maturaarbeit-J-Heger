import random
from class_Cubie import *
import numpy as np
import matplotlib.pyplot as plt








#::::::::::::::::::::::::::::::::::::::::::::::::::: LBL-Method ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




def solveLBLcross(scr):
    cross_solution = ["X", "X"]
    cube1.reset()
    #print(scr)
    cube1.doalg(scr + cross_solution)
    #print("the scramble:")
    #cube1.virtualcube()
    white_edges_positions = list(white_side & edges_set)




    #Solve the cross
    for i in range(4):

        if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
            pass
            #print(f"{white_edges_positions[i]} is solved")
        else:
            position = cube1.cp.index(white_edges_positions[i])
            #print(f"{white_edges_positions[i]} not solved and in place {position}")


            if position in white_layer - white_side:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["R", "L", "B", "F"])
                    random_alg += scramble(1, ["D", "Di", "D2", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += reverse_alg(random_alg[1:2])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
                        #print(random_alg)
                        cross_solution += random_alg
                        #print(cross_solution)
                        #cube1.virtualcube()
                        break
                    else:
                        cube1.cp = sp

            if position in yellow_layer - yellow_side:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["U", "Ui", "U2", ""])
                    cube1.doalg(random_alg)
                    destructive_move1 = cube1.cp
                    cube1.cp = sp
                    random_alg += scramble(1, ["R", "L", "B", "F"])
                    cube1.doalg(random_alg)
                    destructive_move2 = cube1.cp
                    cube1.cp = sp
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += reverse_alg(random_alg[1:2])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i] and destructive_move1[white_edges_positions[i]] == destructive_move2[white_edges_positions[i]]:
                        #print(random_alg)
                        cross_solution += random_alg
                        #print(cross_solution)
                        #cube1.virtualcube()
                        break
                    else:
                        cube1.cp = sp

            if position in yellow_side:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["U", "Ui", "U2", ""])
                    random_alg += scramble(1, ["R2", "L2", "B2", "F2"])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
                        #print(random_alg)
                        cross_solution += random_alg
                        #print(cross_solution)
                        #cube1.virtualcube()
                        break
                    else: cube1.cp = sp

            if position not in white_layer | yellow_layer:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["D", "Di", "D2", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += reverse_alg(random_alg[0:1])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
                        #print(random_alg)
                        cross_solution += random_alg
                        #print(cross_solution)
                        #cube1.virtualcube()
                        break
                    else: cube1.cp = sp

            if position in white_side:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["R", "L", "B", "F"])
                    random_alg += scramble(1, ["D", "Di", "D2", ""])
                    random_alg += reverse_alg(random_alg[0:1])
                    random_alg += reverse_alg(random_alg[1:2])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
                        #print(random_alg)
                        cross_solution += random_alg
                        #print(cross_solution)
                        #cube1.virtualcube()
                        break
                    else:
                        cube1.cp = sp

    cross_solution = [elem for elem in cross_solution if elem != ""]
    #print(cross_solution)
    #print(len(cross_solution))
    #cube1.virtualcube()
    return cross_solution

def solveLBLwhite_corners(scr):
    white_face_solution = [] # Die totale Lösung des Schritts
    cube1.reset()
    cube1.doalg(scr)
    white_corner_positions = list(white_side & corners_set) # Eine Liste der Nummern der weissen Ecksteine
    for i in range(4): # Die vier Ecksteine werden nacheinander gelöst
        if cube1.cp[white_corner_positions[i]] == white_corner_positions[i]:# Falls der Stein bereits gelöst ist, wird der Teilschritt übersprungen
            pass
        else: # Wenn der Eckstein nicht gelöst ist
            position = cube1.cp.index(white_corner_positions[i]) # Die Position eines Ecksteins wird bestimmt
            if position in yellow_layer - yellow_side: # Falls sich der Stein in einem bestimmten Bereich befindet
                sp = cube1.cp  # Die Konfiguration zu Beginn des Schritts wird gespeichert
                while True: # Die folgenden Schritte werden so lange wiederholt, bis eine Lösung gefunden wird
                    random_alg = scramble(1, ["U", "Ui", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += scramble(1, ["U", "Ui", ""])
                    random_alg += reverse_alg(random_alg[1:2]) # Ein zufälliger Algorithmus wird generiert, der einem genauen Muster entspricht
                    cube1.doalg(random_alg) # Der Algorithmus wird ausgeführt
                    if cube1.cp[white_corner_positions[i]] == white_corner_positions[i]: # Falls der Stein gelöst wurde
                        white_face_solution += random_alg # Der passende Algorithmus wird zur Lösung hinzugefügt
                        break # Austritt aus der While-Schleife
                    else: # Falls der Stein nicht gelöst ist
                        cube1.cp = sp # Der nicht passende Algorithmus wird rückgängig gemacht und die While-Schleife beginnt erneut

            if position in yellow_side:
                while True:
                    sp = cube1.cp
                    solved_white_corners = 0
                    for pos in white_corner_positions:
                        if sp[pos] == pos:
                            solved_white_corners +=1
                    starting_solved_white_corners = solved_white_corners
                    random_alg = scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    d1 = cube1.cp
                    random_alg += scramble(1, ["U", "Ui", "U2", ""])
                    random_alg += reverse_alg(random_alg[0:1])
                    random_alg += scramble(1, ["U", "Ui", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += scramble(1, ["U", "Ui", ""])
                    random_alg += reverse_alg(random_alg[4:5])
                    cube1.doalg(random_alg)

                    solved_white_corners = 0
                    for pos in white_corner_positions:
                        if cube1.cp[pos] == pos:
                            solved_white_corners += 1
                    if cube1.cp[white_corner_positions[i]] == white_corner_positions[i] \
                            and sp[white_corner_positions[i]] == d1[white_corner_positions[i]]\
                            and starting_solved_white_corners < solved_white_corners:
                        white_face_solution += random_alg
                        break
                    else:
                        cube1.cp = sp
            if position in white_layer:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["R", "L", "B", "F"])
                    random_alg += scramble(1, ["U", "Ui", ""])
                    random_alg += reverse_alg(random_alg[0:1])
                    random_alg += scramble(1, ["U", "Ui", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += scramble(1, ["U", "Ui", ""])
                    random_alg += reverse_alg(random_alg[4:5])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_corner_positions[i]] == white_corner_positions[i]:
                        white_face_solution += random_alg
                        break
                    else:
                        cube1.cp = sp
    white_face_solution = [elem for elem in white_face_solution if elem != ""]
    return white_face_solution

def solveLBLmiddle_layer(scr):
    middle_layer_solution = ["X", "X"]
    cube1.reset()
    cube1.doalg(scr + middle_layer_solution)
    middle_layer_corner_positions = list(edges_set - yellow_layer - white_layer - blue_side - green_side)
    #print(middle_layer_corner_positions)

    a = [[lblalg1.alg], [["Y", "Y", "Y"] + lblalg2.alg], [["Y"] + lblalg3.alg], [["Y", "Y"] + lblalg4.alg],
         [["Y", "Y", "Y"] + lblalg5.alg], [[""] + lblalg6.alg],
         [["Y", "Y"] + lblalg7.alg], [["Y"] + lblalg8.alg]]
    a = [[lblalg1.alg], [lblalg2.alg], [lblalg3.alg], [lblalg4.alg],
         [lblalg5.alg], [lblalg6.alg],
         [lblalg7.alg], [lblalg8.alg]]



    totalattempts = 0
    while not all(cube1.cp[position] == position for position in middle_layer_corner_positions):
        totalattempts += 1
        #print(f"---------------------------------for i in range(4) start-------------{totalattempts}-----------------------------------------")
        for i in range(4):
            if cube1.cp[middle_layer_corner_positions[i]] == middle_layer_corner_positions[i]:
                #print(middle_layer_corner_positions[i], "is solved")
                pass
            else:
                #print(middle_layer_corner_positions[i], "is not solved and is in position",
                      #cube1.cp.index(middle_layer_corner_positions[i]))
                position = cube1.cp.index(middle_layer_corner_positions[i])
                if position in yellow_layer:
                    #print("case yellow_side")
                    sp = cube1.cp
                    correct_pieces = 0
                    for k in range(4):
                        if cube1.cp[middle_layer_corner_positions[k]] == middle_layer_corner_positions[k]:
                            correct_pieces += 1
                    starting_correct_pieces = correct_pieces
                    while True:
                        random_alg = []
                        random_alg += [scramble(1, ["U", "Ui", "U2", ""])]
                        random_alg += random.choice(a)
                        random_alg += [[""]]
                        random_alg = sum(random_alg, [])

                        #print(spell_alg(random_alg),"  \t|\t", cube1.cp[middle_layer_corner_positions[i]], middle_layer_corner_positions[i], end="\t|\tafter alg  |  ")
                        cube1.doalg(random_alg)
                        #print(cube1.cp[middle_layer_corner_positions[i]], middle_layer_corner_positions[i])

                        correct_pieces = 0
                        for k in range(4):
                            if cube1.cp[middle_layer_corner_positions[k]] == middle_layer_corner_positions[k]:
                                correct_pieces += 1
                        ending_correct_pieces = correct_pieces

                        if cube1.cp[middle_layer_corner_positions[i]] == middle_layer_corner_positions[i] and starting_correct_pieces < ending_correct_pieces:
                            #print(random_alg)
                            middle_layer_solution += random_alg
                            #print(middle_layer_solution)
                           #cube1.virtualcube()
                            break
                        else:
                            cube1.cp = sp

                #if False:
                if position not in yellow_layer and not (yellow_layer - yellow_side) & set(middle_layer_corner_positions) & edges_set:
                    #print("case in middle layer")
                    correct_pieces = 0
                    for k in range(4):
                        if cube1.cp[middle_layer_corner_positions[k]] == middle_layer_corner_positions[k]:
                            correct_pieces += 1
                    starting_correct_pieces = correct_pieces
                    while True:
                        sp = cube1.cp
                        random_alg = []
                        random_alg += random.choice(a)
                        random_alg += [scramble(1, ["U", "Ui", "U2", ""])]
                        random_alg += random.choice(a)
                        random_alg = sum(random_alg, [])
                        cube1.doalg(random_alg)
                        #print("///random_alg///", spell_alg(random_alg))
                        correct_pieces = 0
                        for k in range(4):
                            if cube1.cp[middle_layer_corner_positions[k]] == middle_layer_corner_positions[k]:
                                correct_pieces += 1
                        ending_correct_pieces = correct_pieces
                        if cube1.cp[middle_layer_corner_positions[i]] == middle_layer_corner_positions[i] and starting_correct_pieces < ending_correct_pieces:
                            #print("....", random_alg)
                            middle_layer_solution += random_alg
                            #print(middle_layer_solution)
                            #cube1.virtualcube()
                            break
                        else:
                            cube1.cp = sp


    middle_layer_solution = [elem for elem in middle_layer_solution if elem != ""]
    #print(middle_layer_solution)
    #print(len(middle_layer_solution))
    #cube1.virtualcube()
    return middle_layer_solution

def solveLBLyellow_cross_partI(scr):
    #print("Yellow cross start")
    yellow_cross_solution_partI = []
    cube1.reset()
    cube1.doalg(scr)
    yellow_edges_positions = list(yellow_side & edges_set)
    #print(yellow_edges_positions)
    sp = cube1.cp

    while True:
        correct_pieces = 0
        for k in range(4):
            if cube1.cp[yellow_edges_positions[k]] in yellow_edges_positions:
                correct_pieces += 1
        starting_correct_pieces = correct_pieces
        #
        count = 0
        for elem in list(yellow_side & edges_set - red_layer - orange_layer):
            if cube1.cp[elem] in yellow_side:
                count += 1

        if starting_correct_pieces == 0:
            #print("CASE: starting_correct_pieces == 0")
            cube1.doalg(fsexymove)
            yellow_cross_solution_partI += fsexymove
            #print(yellow_cross_solution_partI)
            for k in range(4):
                if cube1.cp[yellow_edges_positions[k]] in yellow_edges_positions:
                    correct_pieces += 1
            ending_correct_pieces = correct_pieces
            #print(f"------------ ending_correct_pieces = {ending_correct_pieces}")



        elif starting_correct_pieces == 2 and count == 2 or count == 0:
            #print("THE CASE HAPPENED!!!!!!!!!!!!!!!!")
            while True:
                cube1.cp = sp
                cube1.doalg(yellow_cross_solution_partI)
                random_alg = []
                random_alg += scramble(1, ["U", ""])
                random_alg += fsexymove
                cube1.doalg(random_alg)
                correct_pieces = 0
                for k in range(4):
                    if cube1.cp[yellow_edges_positions[k]] in yellow_edges_positions:
                        correct_pieces += 1
                ending_correct_pieces = correct_pieces
                if ending_correct_pieces == 4:
                    yellow_cross_solution_partI += random_alg
                    #print(random_alg, "_______-------")
                    break

        elif starting_correct_pieces == 2:
            #print("CASE: starting_correct_pieces == 2")
            while True:
                cube1.cp = sp
                cube1.doalg(yellow_cross_solution_partI)
                random_alg = []
                random_alg += scramble(1, ["U", "Ui", "U2", ""])
                #random_alg += random.choice([["y"], ["y", "y"], ["y", "y", "y"], []])
                random_alg += random.choice([fsexymove, ["F"]+(sexymove)*2+["Fi"]])
                cube1.doalg(random_alg)
                correct_pieces = 0
                for k in range(4):
                    if cube1.cp[yellow_edges_positions[k]] in yellow_edges_positions:
                        correct_pieces += 1
                ending_correct_pieces = correct_pieces
                if ending_correct_pieces == 4:
                    yellow_cross_solution_partI += random_alg
                    #print(random_alg, "_______-------")
                    break


        elif starting_correct_pieces == 4:
            #print("CASE: starting_correct_pieces == 4")
            #print(yellow_cross_solution_partI)
            #cube1.virtualcube()

            yellow_cross_solution_partI = [elem for elem in yellow_cross_solution_partI if elem != ""]
            #print(yellow_cross_solution_partI)
            #print(len(yellow_cross_solution_partI))
            #cube1.virtualcube()
            break

    return yellow_cross_solution_partI

def solveLBLyellow_cross_partII(scr):
    #print("Yellow cross part II start")
    yellow_cross_solution_partII = []
    cube1.reset()
    cube1.doalg(scr)
    yellow_edges_positions = list(yellow_side & edges_set)
    #print(yellow_edges_positions)
    sp = cube1.cp


    pseudo_correct_elements = 0
    for option in ["U", "Ui", "U2", ""]:
        cube1.cp = sp
        cube1.doalg([option])
        correct_pieces = 0
        for k in range(4):
            if cube1.cp[yellow_edges_positions[k]] == yellow_edges_positions[k]:
                correct_pieces += 1
        if correct_pieces > pseudo_correct_elements:
            pseudo_correct_elements = correct_pieces
    #print("pseudo_correct_elements", pseudo_correct_elements)
    cube1.cp = sp

    #Testing wether it needs one sune or two
    cube1.cp = sp
    cube1.doalg(["R2", "L2", "D2", "R2", "L2"])
    angle_pieces = 0
    pseudo_angle_pieces = 0
    for option in ["U", "Ui", "U2", ""]:

        cube1.doalg([option])
        correct_pieces = 0
        for k in range(4):
            if cube1.cp[yellow_edges_positions[k]] == yellow_edges_positions[k]:
                correct_pieces += 1
        #print(correct_pieces)
        if correct_pieces > pseudo_angle_pieces:
            pseudo_angle_pieces = correct_pieces

    if pseudo_angle_pieces > angle_pieces:
        angle_pieces = pseudo_angle_pieces

    if angle_pieces == 0:
        angle_pieces = 4
    #print("angle_pieces", angle_pieces)
    cube1.cp = sp

    if pseudo_correct_elements == 4:
        while True:
            random_alg = scramble(1, ["U", "Ui", "U2", ""])
            #print(random_alg)
            cube1.doalg(random_alg)
            correct_pieces = 0
            for k in range(4):
                if cube1.cp[yellow_edges_positions[k]] == yellow_edges_positions[k]:
                    correct_pieces += 1
            ending_correct_pieces = correct_pieces

            #print(f"------------ ending_correct_pieces = {ending_correct_pieces}")
            if ending_correct_pieces == 4:
                yellow_cross_solution_partII += random_alg
                yellow_cross_solution_partII = [elem for elem in yellow_cross_solution_partII if elem != ""]
                #print("yellow_cross_solution_partII", yellow_cross_solution_partII)
                #print(len(yellow_cross_solution_partII))
                #cube1.virtualcube()
                break
            else:
                cube1.cp = sp


    elif pseudo_correct_elements != 4 and angle_pieces != 4:
        while True:
            correct_pieces = 0
            for k in range(4):
                if cube1.cp[yellow_edges_positions[k]] == yellow_edges_positions[k]:
                    correct_pieces += 1
            starting_correct_pieces = correct_pieces
            #print(f"------------ starting_correct_pieces = {starting_correct_pieces}")

            random_alg = []
            random_alg += scramble(1, ["U", "Ui", "U2", ""])
            random_alg += sune
            random_alg += scramble(1, ["U", "Ui", "U2", ""])

            #print(random_alg)
            cube1.doalg(random_alg)
            correct_pieces = 0
            for k in range(4):
                if cube1.cp[yellow_edges_positions[k]] == yellow_edges_positions[k]:
                    correct_pieces += 1
            ending_correct_pieces = correct_pieces

            #print(f"------------ ending_correct_pieces = {ending_correct_pieces}")


            if ending_correct_pieces == 4:
                yellow_cross_solution_partII += random_alg
                yellow_cross_solution_partII = [elem for elem in yellow_cross_solution_partII if elem != ""]
                #print("yellow_cross_solution_partII", yellow_cross_solution_partII)
                #print(len(yellow_cross_solution_partII))
                #cube1.virtualcube()
                break
            else:
                cube1.cp = sp

    elif pseudo_correct_elements != 4 and angle_pieces == 4:
        while True:
            correct_pieces = 0
            for k in range(4):
                if cube1.cp[yellow_edges_positions[k]] == yellow_edges_positions[k]:
                    correct_pieces += 1
            starting_correct_pieces = correct_pieces
            #print(f"------------ starting_correct_pieces = {starting_correct_pieces}")

            random_alg = []
            random_alg += sune
            random_alg += scramble(1, ["U", "Ui", "U2", ""])
            random_alg += sune
            random_alg += scramble(1, ["U", "Ui", "U2", ""])

            #print(random_alg)
            cube1.doalg(random_alg)
            correct_pieces = 0
            for k in range(4):
                if cube1.cp[yellow_edges_positions[k]] == yellow_edges_positions[k]:
                    correct_pieces += 1
            ending_correct_pieces = correct_pieces

            #print(f"------------ ending_correct_pieces = {ending_correct_pieces}")


            if ending_correct_pieces == 4:
                yellow_cross_solution_partII += random_alg
                yellow_cross_solution_partII = [elem for elem in yellow_cross_solution_partII if elem != ""]
                #print("yellow_cross_solution_partII", yellow_cross_solution_partII)
                #print(len(yellow_cross_solution_partII))
                #cube1.virtualcube()
                break
            else:
                cube1.cp = sp

    return yellow_cross_solution_partII

def solveLBLyellow_corner_positions(scr):
    #print("yellow_corner_positions start")
    yellow_corner_positions_solution = []
    cube1.reset()
    cube1.doalg(scr)
    sp = cube1.cp

    if cube1.cp[list(yellow_layer & red_layer & green_layer)[0]] in yellow_layer & red_layer & green_layer \
            and cube1.cp[list(yellow_layer & red_layer & blue_layer)[0]] in yellow_layer & red_layer & blue_layer \
            and cube1.cp[list(yellow_layer & orange_layer & green_layer)[0]] in yellow_layer & orange_layer & green_layer \
            and cube1.cp[list(yellow_layer & orange_layer & blue_layer)[0]] in yellow_layer & orange_layer & blue_layer:
        #print("Step already completed")
        return []

    if cube1.cp[list(yellow_layer & red_layer & green_layer)[0]] in yellow_layer & red_layer & green_layer:
        needed_breakdance_count = 1
    elif cube1.cp[list(yellow_layer & red_layer & blue_layer)[0]] in yellow_layer & red_layer & blue_layer:
        needed_breakdance_count = 1
    elif cube1.cp[list(yellow_layer & orange_layer & green_layer)[0]] in yellow_layer & orange_layer & green_layer:
        needed_breakdance_count = 1
    elif cube1.cp[list(yellow_layer & orange_layer & blue_layer)[0]] in yellow_layer & orange_layer & blue_layer:
        needed_breakdance_count = 1
    else:
        needed_breakdance_count = 2
    #print("needed_breakdance_count", needed_breakdance_count)




    if needed_breakdance_count == 1:
        while True:
            cube1.cp = sp
            random_alg = scramble(1, ["", "U", "Ui", "U2"])
            random_alg += breakdance
            random_alg += random.choice(["", breakdance])
            random_alg += reverse_alg(random_alg[0:1])
            cube1.doalg(random_alg)


            if cube1.cp[list(yellow_layer & red_layer & green_layer)[0]] in yellow_layer & red_layer & green_layer\
                    and cube1.cp[list(yellow_layer & red_layer & blue_layer)[0]] in yellow_layer & red_layer & blue_layer\
                    and cube1.cp[list(yellow_layer & orange_layer & green_layer)[0]] in yellow_layer & orange_layer & green_layer\
                    and cube1.cp[list(yellow_layer & orange_layer & blue_layer)[0]] in yellow_layer & orange_layer & blue_layer:
                # print("")
                #print(random_alg)
                #cube1.virtualcube()
                yellow_corner_positions_solution += random_alg
                break

    if needed_breakdance_count == 2:
        while True:
            cube1.cp = sp
            random_alg = []
            random_alg += breakdance
            setup_move = scramble(1, ["", "U", "Ui", "U2"])
            random_alg += setup_move
            random_alg += breakdance
            random_alg += random.choice(["", breakdance])
            random_alg += reverse_alg(setup_move)
            #random_alg += reverse_alg(random_alg[7:8])
            #print(random_alg)
            cube1.doalg(random_alg)

            if cube1.cp[list(yellow_layer & red_layer & green_layer)[0]] in yellow_layer & red_layer & green_layer\
                    and cube1.cp[list(yellow_layer & red_layer & blue_layer)[0]] in yellow_layer & red_layer & blue_layer\
                    and cube1.cp[list(yellow_layer & orange_layer & green_layer)[0]] in yellow_layer & orange_layer & green_layer\
                    and cube1.cp[list(yellow_layer & orange_layer & blue_layer)[0]] in yellow_layer & orange_layer & blue_layer:
                # print("")
                #print(random_alg)
                #cube1.virtualcube()
                yellow_corner_positions_solution += random_alg
                break

    return yellow_corner_positions_solution

def solveLBLfinal_step(scr):
    #print("Final step start")
    final_step_solution = ["X", "X"]
    cube1.reset()
    cube1.doalg(scr + final_step_solution)
    sp = cube1.cp

    if cube1.cp == op:
        #print("Step already completed")
        return []

    #cube1.virtualcube()

    while True:
        if cube1.cp[list(yellow_side & red_layer & green_layer)[0]] == list(yellow_side & red_layer & green_layer)[0]:
            break
        else:
            final_step_solution += bottom_sexymove*2
            cube1.doalg(bottom_sexymove*2)



    cube1.doalg(["U"])
    final_step_solution += ["U"]

    while True:
        if cube1.cp[list(yellow_side & red_layer & green_layer)[0]] == list(yellow_side & orange_layer & green_layer)[0]:
            break
        else:
            final_step_solution += bottom_sexymove * 2
            cube1.doalg(bottom_sexymove * 2)


    cube1.doalg(["U"])
    final_step_solution += ["U"]
    while True:
        if cube1.cp[list(yellow_side & red_layer & green_layer)[0]] == list(yellow_side & orange_layer & blue_layer)[0]:
            break
        else:
            final_step_solution += bottom_sexymove * 2
            cube1.doalg(bottom_sexymove * 2)

    cube1.doalg(["U"])
    final_step_solution += ["U"]
    while True:
        if cube1.cp[list(yellow_side & red_layer & green_layer)[0]] == list(yellow_side & red_layer & blue_layer)[0]:
            break
        else:
            final_step_solution += bottom_sexymove * 2
            cube1.doalg(bottom_sexymove * 2)
    cube1.doalg(["U"])
    final_step_solution += ["U"]

    #cube1.virtualcube()
    return final_step_solution

def solveLBL(scr, print_solution = False):
    LBLsolution = []
    if print_solution:
        cube1.reset().doalg(scr).virtualcube().reset()
    LBLsolution += [" | "] + solveLBLcross(scr)
    LBLsolution += [" | "] + solveLBLwhite_corners(scr + LBLsolution)
    LBLsolution += [" | "] + solveLBLmiddle_layer(scr + LBLsolution)
    LBLsolution += [" | "] + solveLBLyellow_cross_partI(scr + LBLsolution)
    LBLsolution += [" | "] + solveLBLyellow_cross_partII(scr + LBLsolution)
    LBLsolution += [" | "] + solveLBLyellow_corner_positions(scr + LBLsolution)
    LBLsolution += [" | "] + solveLBLfinal_step(scr + LBLsolution)



    if print_solution:

        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)[0]}"
            f"\nThe \033[0;34m{spell_alg(LBLsolution)[1]}\033[0m-move solution with"
            f" \033[0;34m{spell_alg(LBLsolution)[2]}\033[0m cube rotations is: {spell_alg(LBLsolution)[0]}\n")
        #LBLsolutionAlg = Alg(LBLsolution)
        #LBLsolutionAlg.correct()
        #print("cancel moves out:", spell_alg(LBLsolutionAlg.alg)[1])
        #count_moves(LBLsolutionAlg.alg)

        print("-" * 143)

    data = spell_alg(LBLsolution, short_version=True)
    return data



#cube1.virtualcube()
solveLBL(scramble(20), True)

"""
#with open("solves_data/scrambles_list.txt", "r") as file:
    lines = file.readlines()

all_scrambles = []
for line in lines:
    all_scrambles.append(eval(line.strip()))



with open("solves_data/LBL_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveLBL(scr, False)))+"\n")
"""

########################################################################################################################
##################################                                                      ################################
##############################                      Diagramm erstellen                       ###########################


"""
# Daten erstellen
y_values = []
for i in range(1000):
    print(i)
    y_values.append(solveLBL(scramble(40))[1])

# Durchschnitt, Maximum und Minimum berechnen
avg_y = sum(y_values) / len(y_values)
max_y = max(y_values)
min_y = min(y_values)
print("Durchschnittlicher y-Wert:", avg_y)
print("Maximum y-Wert:", max_y)
print("Minimum y-Wert:", min_y)

# Diagramm erstellen
plt.plot(y_values)

# Trendlinie berechnen
trendline = np.polyfit(range(len(y_values)), y_values, 1)
y_trendline = np.polyval(trendline, range(len(y_values)))
plt.plot(y_trendline, 'r--')

# Grüne Linie mit solveLBL(scramble(40))[1]-Werten
y_green = [solveLBL(scramble(40))[2] for i in range(1000)]
plt.plot(y_green, 'g-')

# y-Achse auf Bereich von 0 bis 250 beschränken
plt.ylim([0, 250])

plt.xlabel('Versuche')
plt.ylabel('Anzahl Züge')
plt.title('Anzahl Züge für die LBL-Methode')

# Diagramm in der Konsole anzeigen
plt.show()

"""
