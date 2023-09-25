import random
from class_Cubie import *
import numpy as np
import matplotlib.pyplot as plt



#::::::::::::::::::::::::::::::::::::::::::::::::::: LBL-Method ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


def solveCFOPcross(scr):
    cross_solution = []
    cube1.reset()
    print("scramble:", (scr))
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

def solveCFOPF2L(scr):
    F2L_solution = []
    cube1.reset().doalg(scr).virtualcube()

    pair1 = (6, 11, 20, 29, 35)
    pair2 = (10, 14, 21, 33, 39)
    pair3 = (19, 7, 22, 41, 31)
    pair4 = (15, 18, 23, 37, 43)

    not_solved_pairs = [pair1, pair2, pair3, pair4]
    not_solved_pairs = [pair for pair in not_solved_pairs if not all(cube1.is_position_solved(elem) for elem in pair)]
    print(not_solved_pairs)

    def on_which_side(pos):
        if pos in white_side: return "w"
        elif pos in yellow_side: return "y"
        elif pos in orange_side: return "o"
        elif pos in red_side: return "r"
        elif pos in blue_side: return "b"
        elif pos in green_side: return "g"

    def count_solved_pairs():
        solved_pairs = 4 - len([pair for pair in [pair1, pair2, pair3, pair4] if not all(cube1.is_position_solved(elem) for elem in pair)])
        return solved_pairs


    def analyse_pair_position(pair):
        sidelist = []
        for elem in pair:
            sidelist += [on_which_side(elem)]
        #print(sidelist)
        unique_set = set()
        sidelist = [x for x in sidelist if not (x in unique_set or unique_set.add(x))]

        #print(f"{pair[1] in yellow_side} and {pair[3] in yellow_side} and not {(opposit_side(on_which_side(pair[2])) in sidelist)} and not (len({sidelist})==3")
        print(pair[2] in yellow_side, pair[4] in [43, 31, 35, 39])
        print(pair[4])
        #return | are adjacent | corner on top layer| edge on top layer | corner on top side | corner solved | is paired | worst case | 3move pair | triple sexy pair case
        return [len(sidelist) == 3, pair[0] in yellow_layer, pair[4] in yellow_layer, pair[2] in yellow_side,
                cube1.is_position_solved(pair[2]),
                on_which_side(pair[1]) == on_which_side(pair[4]) and on_which_side(pair[0]) == on_which_side(pair[3]),
                pair[2] in yellow_side and ((on_which_side(pair[1]) == on_which_side(pair[4]))^(on_which_side(pair[0]) == on_which_side(pair[3]))),
                ((pair[1] in yellow_side and pair[3] in yellow_side) or (pair[0] in yellow_side and pair[4] in yellow_side))
                and (not (opposit_side(on_which_side(pair[2])) in sidelist)) and (not (len(sidelist)==3)),
                pair[2] in yellow_side and pair[4] in [43, 31, 35, 39]]

    while len(not_solved_pairs) > 0:
        pair_positions = [[cube1.cp.index(elem) for elem in pair] for pair in not_solved_pairs]
        #print(pair_positions)
        app_list = [analyse_pair_position(pair) for pair in pair_positions]
        #print(app_list)
        starting_correct_pairs = count_solved_pairs()
        pair_changed = False
        if pair_changed == False:                           #case1 free pair
            for app, pair in zip(app_list, not_solved_pairs):
                if (app[1] and app[2] and app[5]) or app[7]:
                    #print(app)
                    #print("case1 free pair occured", pair)
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case2 paired in layer
            for app, pair in zip(app_list, not_solved_pairs):
                if app[5]:
                    #print("case2 paired in layer occured", pair)
                    sp = cube1.cp
                    while True:
                        random_alg = pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if (cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer)\
                                and starting_correct_pairs == count_solved_pairs():
                            #print("if-statement is True")
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                #print("now we have constructed a free pair", random_alg)
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp

                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case3 both on top
            for app, pair in zip(app_list, not_solved_pairs):
                if app[1] and app[2] and not app[6]:
                    #print("case3 both on top occured", pair)
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            #print("if-statement is True")
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            #print(step_app)
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                #print("now we have constructed a free pair", random_alg)
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp

                    sp = cube1.cp
                    while True:
                        random_alg = []
                        random_alg += scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case4 one on top
            for app, pair in zip(app_list, not_solved_pairs):
                if app[1] ^ app[2] and not app[8]:
                    #print("case4 one on top occured", pair)
                    sp = cube1.cp

                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            #print("if-statement is True")
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                #print("now we have constructed a free pair", random_alg)
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp

                    sp = cube1.cp
                    while True:
                        random_alg = []
                        random_alg += scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case5 both down, worst case, or triple sexy pair
            for app, pair in zip(app_list, not_solved_pairs):
                if (not app[1] and not app[2]) or app[6] or app[8]:
                    #print("case5 both down/worst case occured", pair)
                    sp = cube1.cp
                    while True:
                        random_alg = pair_insertion()
                        random_alg += scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            #print("if-statement is True")
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if ((step_app[1] and step_app[2] and step_app[5]) or step_app[7]) and (count_solved_pairs() == starting_correct_pairs):
                                #print("now we have constructed a free pair", random_alg)
                                #print(count_solved_pairs(), starting_correct_pairs)
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp

                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        #print(random_alg)
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break



        F2L_solution += [" | "]
        #print("count_solved_pairs()", count_solved_pairs())
        cube1.virtualcube()
        not_solved_pairs = [pair for pair in not_solved_pairs if not all(cube1.is_position_solved(elem) for elem in pair)]






    F2L_solution = [elem for elem in F2L_solution if elem != ""]
    #print("count_solved_pairs()", count_solved_pairs())
    return F2L_solution

def solveCFOPOLL(scr):            # ORIENTATION OF THE LAST LAYER
    OLLsolution = []
    cube1.reset()
    print("scramble:", (scr))
    cube1.doalg(scr + OLLsolution)
    # print("the scramble:")
    # cube1.virtualcube()
    yellow_edges = yellow_side & edges_set
    yellow_corners = yellow_side & corners_set
    yellow_edges_count = sum(cube1.cp[elem] in yellow_edges for elem in yellow_edges)
    yellow_corner_count = sum(cube1.cp[elem] in yellow_corners for elem in yellow_corners)
    count = yellow_edges_count + yellow_corner_count + 1
    if count == 9:
        print("OLL is done!")
    else:
        minus_shape = False
        if (cube1.cp[24] in yellow_side and cube1.cp[26] in yellow_side)\
                ^(cube1.cp[25] in yellow_side and cube1.cp[27] in yellow_side):
            minus_shape = True

        if yellow_edges_count == 0 and yellow_corner_count < 2:
            print("case1")

            sp = cube1.cp
            breakvariable = False
            for oll in oll_group1:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break


        elif yellow_edges_count == 2 and yellow_corner_count == 0 and not minus_shape: # clock!!!
            print("case2")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group2:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 2 and yellow_corner_count == 1 and not minus_shape: # clock!!!
            print("case3")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group3:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 2 and yellow_corner_count == 2 and not minus_shape: # clock!!!
            print("case4")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group4:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 2 and yellow_corner_count == 0 and minus_shape: # minus
            print("case5")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group5:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 2 and yellow_corner_count == 1 and minus_shape: # minus
            print("case6")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group6:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 2 and yellow_corner_count == 2 and minus_shape: # minus
            print("case7")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group7:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 0:
            print("case8")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group8:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 4 and yellow_corner_count < 2:
            print("case9")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group9:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 4 and yellow_corner_count == 2:
            print("case10")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group10:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        elif yellow_edges_count == 2 and yellow_corner_count == 4:
            print("case11")
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group11:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        print("OLL solved with the alg:", alg)
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable: break

        else: print("no matching case found")


    OLLsolution = [elem for elem in OLLsolution if elem != ""]
    # print(cross_solution)
    # print(len(cross_solution))
    # cube1.virtualcube()
    return OLLsolution

def solveCFOPPLL(scr):  # PERMUTATION OF THE LAST LAYER
    PLLsolution = []
    cube1.reset()
    print("scramble:", (scr))
    cube1.doalg(scr + PLLsolution)
    # print("the scramble:")
    # cube1.virtualcube()
    correct_yellow_pieces = sum(cube1.cp[elem] == elem for elem in yellow_side)

    print(correct_yellow_pieces)

    if correct_yellow_pieces == 8:
        print("PLL is done!")
    else:


        if True:
            sp = cube1.cp
            breakvariable = False
            for pll in pll_group:
                for alg in alg_list(pll):
                    cube1.doalg(alg)
                    print(alg)
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        print("PLL solved with the alg:", alg)
                        PLLsolution += alg
                        breakvariable = True
                        break
                    cube1.doalg("U")
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        print("PLL solved with the alg:", alg)
                        PLLsolution += alg + ["U"]
                        breakvariable = True
                        break
                    cube1.doalg("U")
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        print("PLL solved with the alg:", alg)
                        PLLsolution += alg + ["U2"]
                        breakvariable = True
                        break
                    cube1.doalg("U")
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        print("PLL solved with the alg:", alg)
                        PLLsolution += alg + ["Ui"]
                        breakvariable = True
                        break

                    else:
                        cube1.cp = sp
                if breakvariable: break






    PLLsolution = [elem for elem in PLLsolution if elem != ""]
    # print(cross_solution)
    # print(len(cross_solution))
    # cube1.virtualcube()
    return PLLsolution


def solveCFOP(scr, print_solution = False):
    CFOPsolution = []
    if print_solution:
        cube1.reset().doalg(scr).virtualcube().reset()
    CFOPsolution += [" | "] + solveCFOPcross(scr)
    CFOPsolution += [" | "] + solveCFOPF2L(scr + CFOPsolution)
    CFOPsolution += [" | "] + solveCFOPOLL(scr + CFOPsolution)
    CFOPsolution += [" | "] + solveCFOPPLL(scr + CFOPsolution)



    if print_solution:
        cube1.virtualcube()
        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)[0]}"
            f"\nThe \033[0;34m{spell_alg(CFOPsolution)[1]}\033[0m-move solution with"
            f" \033[0;34m{spell_alg(CFOPsolution)[2]}\033[0m cube rotations is: {spell_alg(CFOPsolution)[0]}\n")


        #LBLsolutionAlg = Alg(LBLsolution)
        #LBLsolutionAlg.correct()
        #print("cancel moves out:", spell_alg(LBLsolutionAlg.alg)[1])
        #count_moves(LBLsolutionAlg.alg)

        print("-" * 143)

    data = spell_alg(CFOPsolution, short_version=True)
    #data = CFOPsolution
    return data


"""#with open("solves_data/scrambles_list.txt", "w") as file:
    for i in range(10000):
        file.write(str(scramble(30))+"\n")"""

solveCFOP(scramble(20), True)


"""#with open("solves_data/scrambles_list.txt", "r") as file:
    lines = file.readlines()

all_scrambles = []
for line in lines:
    all_scrambles.append(eval(line.strip()))



with open("solves_data/CFOP_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveCFOP(scr, False)))+"\n")
#"""

"""#with open("solves_data/CFOP_solutions.txt", "r") as file:
    lines = file.readlines()
    all_CFOP_solutions = []
    for line in lines:
        line = line.strip()
        line.replace("yi, ", "'Y', 'Y', 'Y', ")
        line.replace('y', 'Y')
        print("LINE:::::::::::::::", line)
        all_CFOP_solutions.append(eval(line))

mynum = 123

print("SCRAMBLE:", all_scrambles[mynum])
print("SOLUTION:", all_CFOP_solutions[mynum])

cube1.reset()
cube1.doalg(all_scrambles[mynum])
cube1.virtualcube()
cube1.doalg(all_CFOP_solutions[mynum])
cube1.virtualcube()"""


"""
#---------   Own Method Test Area   ---------#
cube1.reset()
cube1.virtualcube()
rotate_alg = ["L", "L", "L", "U", "B", "B", "B", "U", "R", "R", "R", "U", "F", "F", "F", "U"]
reference_list = [27]*3+[24]*4+[25]*4+[26]*4
all_stones_there = set()
for _ in range(2):
    for step, reference in zip(rotate_alg, reference_list):
        cube1.doalg(step)
        all_stones_there.add(cube1.cp[reference])
print(sorted(all_stones_there), len(all_stones_there))
"""





########################################################################################################################
##################################                                                      ################################
##############################                      Diagramm erstellen                       ###########################


"""
# Daten erstellen
y_values = []
for i in range(1000):
    print(i)
    y_values.append(solveCFOP(scramble(40))[1])

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
y_green = [solveCFOP(scramble(40))[2] for i in range(1000)]
plt.plot(y_green, 'g-')

# y-Achse auf Bereich von 0 bis 250 beschränken
plt.ylim([0, 100])

plt.xlabel('Versuche')
plt.ylabel('Anzahl Züge')
plt.title('Anzahl Züge für die CFOP-Methode')

# Diagramm in der Konsole anzeigen
plt.show()

"""
