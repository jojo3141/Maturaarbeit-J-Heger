import random
from Class_Cube import *
import numpy as np
import matplotlib.pyplot as plt





#:::::::::::::::::::::::::::::::::::::::::::::::::: Brute-Force in Steps ::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def solve3pieces(alg):
    for i in range(100000):
        random_alg = scramble(6)
        cube1.doalg(alg + random_alg)
        if cube1.cp[0] == 0 and cube1.cp[1] == 1 and cube1.cp[2] == 2:
            #cube1.virtualcube()
            mark_equal_elements_of_two_lists(op, cube1.cp)
            break

def solve5(scr, attempts_per_step, move_depth):
    cube1.reset()
    cube1.doalg(scr)
    position_after_scramble = cube1.cp
    starting_correct_stickers = check_common_elements(cube1.cp, op)
    correct_stickers = starting_correct_stickers
    print("\033[32m", correct_stickers, "\033[0m")
    for i in range(attempts_per_step):
        random_alg = scramble(move_depth)
        cube1.cp = position_after_scramble
        cube1.doalg(random_alg)
        if check_common_elements(cube1.cp, op) > correct_stickers:
            correct_stickers = check_common_elements(cube1.cp, op)
            best_alg = random_alg
            print(best_alg, correct_stickers)
    if correct_stickers > starting_correct_stickers:
        return best_alg
    else:
        print(f"Sorry, I couldn't find {move_depth} improving moves")
        return []

def solvein5steps(current_scramble, attempts_per_step = 10000, move_depth = 5, steps = 3):
    scramble_length = len(current_scramble)

    for i in range(steps):
        best_alg = solve5(current_scramble, attempts_per_step, move_depth)
        current_scramble += best_alg

    solution = current_scramble[scramble_length:]
    original_scramble = current_scramble[:scramble_length]


    for i in range((len(current_scramble)-scramble_length)//move_depth+1):
        print("\033[0m", (original_scramble*(0**i) + solution[5*(i-1):5*i]), sep="")
        cube1.reset()
        cube1.doalg(original_scramble + solution[0:5*i])
        #cube1.virtualcube()

    print("\033[0m_" * 145)
    print(f"The original scramble was {original_scramble}")
    print(f"I found this {len(solution)}-move-solution: {solution}")
    cube1.reset()
    cube1.doalg(current_scramble)
    print(f"There are \033[32m{check_common_elements(cube1.cp, op)}\033[0m correct elements")
    print(f"solved corners = {check_common_elements(cube1.cp, corners)//3}\t"
          f"unsolved corners = {8-check_common_elements(cube1.cp, corners)//3}\n"
          f"solved edges = {check_common_elements(cube1.cp, edges)//2}\t"
          f"unsolved edges = {12-check_common_elements(cube1.cp, edges)//2}"
          f"   Total percentage: {round(check_common_elements(cube1.cp, op)/0.48)}%")
    print("_" * 145)




#::::::::::::::::::::::::::::::::::::::::::::::::::: LBL-Method ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




def solveLBLcross(scr):
    cross_solution = []
    cube1.reset()
    #print(scr)
    cube1.doalg(scr)
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
    white_face_solution = []
    cube1.reset()
    cube1.doalg(scr)
    white_corner_positions = list(white_side & corners_set)
    #print(white_corner_positions)
    for i in range(4):
        if cube1.cp[white_corner_positions[i]] == white_corner_positions[i]:
            pass
            #print(white_corner_positions[i], "is solved")
        else:
            #print(white_corner_positions[i], "is not solved and is in position", cube1.cp.index(white_corner_positions[i]))
            position = cube1.cp.index(white_corner_positions[i])
            if position in yellow_layer - yellow_side:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["U", "Ui", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += scramble(1, ["U", "Ui", ""])
                    random_alg += reverse_alg(random_alg[1:2])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_corner_positions[i]] == white_corner_positions[i]:
                        #print(random_alg)
                        white_face_solution += random_alg
                        #print(white_face_solution)
                        #cube1.virtualcube()
                        break
                    else:
                        cube1.cp = sp

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
                    #print(random_alg, starting_solved_white_corners, solved_white_corners)
                    if cube1.cp[white_corner_positions[i]] == white_corner_positions[i] \
                            and sp[white_corner_positions[i]] == d1[white_corner_positions[i]]\
                            and starting_solved_white_corners < solved_white_corners:
                        #print(random_alg)
                        white_face_solution += random_alg
                        #print(white_face_solution)
                        #cube1.virtualcube()
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
                        #print(random_alg)
                        white_face_solution += random_alg
                        #print(white_face_solution)
                        #cube1.virtualcube()
                        break
                    else:
                        cube1.cp = sp
    white_face_solution = [elem for elem in white_face_solution if elem != ""]
    #print(white_face_solution)
    #print(len(white_face_solution))
    #cube1.virtualcube()
    return white_face_solution

def solveLBLmiddle_layer(scr):
    middle_layer_solution = []
    cube1.reset()
    cube1.doalg(scr)
    middle_layer_corner_positions = list(edges_set - yellow_layer - white_layer - blue_side - green_side)
    #print(middle_layer_corner_positions)

    totalattempts = 0
    while not all(cube1.cp[position] == position for position in middle_layer_corner_positions):
        totalattempts +=1
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
                        random_alg += random.choice(
                            [[lblalg1.alg], [lblalg2.alg], [lblalg3.alg], [lblalg4.alg], [lblalg5.alg], [lblalg6.alg],
                             [lblalg7.alg], [lblalg8.alg]])
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
                        random_alg += random.choice(
                            [[lblalg1.alg], [lblalg2.alg], [lblalg3.alg], [lblalg4.alg], [lblalg5.alg], [lblalg6.alg],
                             [lblalg7.alg], [lblalg8.alg]])
                        random_alg += [scramble(1, ["U", "Ui", "U2", ""])]
                        random_alg += random.choice(
                            [[lblalg1.alg], [lblalg2.alg], [lblalg3.alg], [lblalg4.alg], [lblalg5.alg], [lblalg6.alg],
                             [lblalg7.alg], [lblalg8.alg]])
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
                random_alg +=random.choice([fsexymove, ["F"]+(sexymove)*2+["Fi"]])
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
    final_step_solution = []
    cube1.reset()
    cube1.doalg(scr)
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
    cube1.virtualcube()
    LBLsolution += solveLBLcross(scr)
    LBLsolution += solveLBLwhite_corners(scr + LBLsolution)
    LBLsolution += solveLBLmiddle_layer(scr + LBLsolution)
    LBLsolution += solveLBLyellow_cross_partI(scr + LBLsolution)
    LBLsolution += solveLBLyellow_cross_partII(scr + LBLsolution)
    LBLsolution += solveLBLyellow_corner_positions(scr + LBLsolution)
    LBLsolution += solveLBLfinal_step(scr + LBLsolution)




    if print_solution:
        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)}\nThe \033[0;34m{len(LBLsolution)}\033[0m-move solution is: {spell_alg(LBLsolution)}")
        LBLsolutionAlg = Alg(LBLsolution)
        LBLsolutionAlg.correct()
        print(len(LBLsolutionAlg.alg))
        print("-" * 143)

    return LBLsolution



cube1.virtualcube()
solveLBL(scramble(20), True)







########################################################################################################################
##################################                                                      ################################
##############################                      Diagramm erstellen                       ###########################
"""

# Daten erstellen
y_values = []
for i in range(1000):
    print(i)
    y_values.append(len(solveLBL(scramble(40))))


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

# y-Achse auf Bereich von 0 bis 250 beschränken
plt.ylim([0, 250])

plt.xlabel('Versuche')
plt.ylabel('Anzahl Züge')
plt.title('Anzahl Züge für die LBL-Methode')

# Diagramm in der Konsole anzeigen
plt.show()

"""