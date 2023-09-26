import random
from class_Cubie import *
import numpy as np
import matplotlib.pyplot as plt



#::::::::::::::::::::::::::::::::::::::::::::::::::: ROUX-Method ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


def solveROUXbase(scr):
    base_solution = []
    cube1.reset()
    print("scramble:", (scr))
    cube1.doalg(scr + base_solution)
    white_edges_positions = [47,45]



    for i in range(2):

        if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
            pass
        else:
            position = cube1.cp.index(white_edges_positions[i])


            if position in white_layer - white_side:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["R", "L", "B", "F"])
                    random_alg += scramble(1, ["D", "Di", "D2", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += reverse_alg(random_alg[1:2])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
                        base_solution += random_alg
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
                        base_solution += random_alg
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
                        base_solution += random_alg
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
                        base_solution += random_alg
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
                        base_solution += random_alg
                        break
                    else:
                        cube1.cp = sp

    base_solution = [elem for elem in base_solution if elem != ""]
    return base_solution

def solveROUXblocks(scr):
    block_solution = []
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
        unique_set = set()
        sidelist = [x for x in sidelist if not (x in unique_set or unique_set.add(x))]

        #print(f"{pair[1] in yellow_side} and {pair[3] in yellow_side} and not {(opposit_side(on_which_side(pair[2])) in sidelist)} and not (len({sidelist})==3")
        #print(pair[2] in yellow_side, pair[4] in [43, 31, 35, 39])
        #print(pair[4])
        #return | are adjacent | corner on top layer| edge on top layer | corner on top side | corner solved | is paired | worst case | 3move pair | triple sexy pair case | edge in M slice
        return [len(sidelist) == 3, pair[0] in yellow_layer, pair[4] in yellow_layer, pair[2] in yellow_side,
                cube1.is_position_solved(pair[2]),
                on_which_side(pair[1]) == on_which_side(pair[4]) and on_which_side(pair[0]) == on_which_side(pair[3]),
                pair[2] in yellow_side and ((on_which_side(pair[1]) == on_which_side(pair[4]))^(on_which_side(pair[0]) == on_which_side(pair[3]))),
                ((pair[1] in yellow_side and pair[3] in yellow_side) or (pair[0] in yellow_side and pair[4] in yellow_side))
                and (not (opposit_side(on_which_side(pair[2])) in sidelist)) and (not (len(sidelist)==3)),
                pair[2] in yellow_side and pair[4] in [43, 31, 35, 39], pair[4] in white_layer or pair [3] in white_layer]

    while len(not_solved_pairs) > 0:
        pair_positions = [[cube1.cp.index(elem) for elem in pair] for pair in not_solved_pairs]
        #print(pair_positions)
        app_list = [analyse_pair_position(pair) for pair in pair_positions]
        #print(app_list)
        starting_correct_pairs = count_solved_pairs()
        just_a_M_turn = False
        pair_changed = False
        if pair_changed == False:                           #case1 free pair
            for app, pair in zip(app_list, not_solved_pairs):
                if ((app[1] and app[2] and app[5]) or app[7]) and not app[9]:
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
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case2 paired in layer
            for app, pair in zip(app_list, not_solved_pairs):
                if app[5] and not app[9]:
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
                                block_solution += random_alg
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
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case3 both on top
            for app, pair in zip(app_list, not_solved_pairs):
                if (app[1] and app[2] and not app[6]) and not app[9]:
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
                                block_solution += random_alg
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
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case4 one on top
            for app, pair in zip(app_list, not_solved_pairs):
                if (app[1] ^ app[2] and not app[8]) and not app[9]:
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
                                block_solution += random_alg
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
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #case5 both down, worst case, or triple sexy pair
            for app, pair in zip(app_list, not_solved_pairs):
                if ((not app[1] and not app[2]) or app[6] or app[8]) and not app[9]:
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
                                block_solution += random_alg
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
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:                           #edge in M slice
            print("CASE EDGE IN M SLICE")
            for app, pair in zip(app_list, not_solved_pairs):
                if app[9]:
                    #print(cube1.cp.index(pair[4]))
                    if cube1.cp.index(pair[4]) in [34, 44]:
                        cube1.doalg(["Mi"])
                        block_solution += ["Mi"]
                    elif cube1.cp.index(pair[4]) in [42, 46]:
                        cube1.doalg(["M"])
                        block_solution += ["M"]
                    pair_changed = True
                    just_a_M_turn = True
                    print("I did a M turn...")



        if not just_a_M_turn:
            block_solution += [" | "]
        #print("count_solved_pairs()", count_solved_pairs())
        cube1.virtualcube()
        not_solved_pairs = [pair for pair in not_solved_pairs if not all(cube1.is_position_solved(elem) for elem in pair)]


    block_solution = [elem for elem in block_solution if elem != ""]
    #print("count_solved_pairs()", count_solved_pairs())
    return block_solution

def solveROUXcmll(scr):
    CMLLsolution = []
    cube1.reset()
    print("scramble:", (scr))
    cube1.doalg(scr + CMLLsolution)
    # print("the scramble:")
    # cube1.virtualcube()
    yellow_corners = yellow_side & corners_set
    yellow_corner_count = sum(cube1.cp[elem] in yellow_corners for elem in yellow_corners)




    def is_cmll_solved(position_list):
        for num in [0, 1, 2, 3, 45, 47]:
            if position_list[num] != num:
                return False
        print("solved!!!")
        return True

    def before_AUF(position_list):
        sp = position_list
        for turn in ["U", "Ui", "U2", ""]:
            cube1.doalg([turn])
            if is_cmll_solved(cube1.cp):
                #print([turn], "this is the auf that leads to solved")
                cube1.cp = sp
                return [turn]
            cube1.cp = sp


    if before_AUF(cube1.cp):
        print("cmll is done! (yet not auf)")
    else:
        while True:
            if yellow_corner_count == 1:
                print("case1")
                sp = cube1.cp
                breakvariable = False
                for cmll in cmll_group1:
                    for alg in alg_list(cmll):
                        cube1.doalg(alg)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            cube1.virtualcube()
                            print("CMLL solved with the alg:", alg)
                            CMLLsolution += alg
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable: break

            elif yellow_corner_count in [0, 4]:

                print("case2")
                sp = cube1.cp
                breakvariable = False
                for cmll in cmll_group2:
                    for alg in alg_list(cmll):
                        cube1.doalg(alg)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            cube1.virtualcube()
                            print("CMLL solved with the alg:", alg)
                            CMLLsolution += alg
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable: break

            elif yellow_corner_count == 2:
                print("case3, 2 yellow corners")
                sp = cube1.cp
                breakvariable = False
                for cmll in cmll_group3:
                    for alg in alg_list(cmll):
                        cube1.doalg(alg)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            cube1.virtualcube()
                            print("CMLL solved with the alg:", alg)
                            CMLLsolution += alg
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable: break

            if not before_AUF(cube1.cp):
                print("no matching case found", "#Problem "*100)
                cube1.doalg(["U"])
                CMLLsolution += ["U"]
            else:
                break


    CMLLsolution = [elem for elem in CMLLsolution if elem != ""]
    print("CMLLsolution:", CMLLsolution)
    # print(len(cross_solution))
    cube1.virtualcube()
    return CMLLsolution

def solveROUXEO(scr):  # Edge Orientation of the Last 6 Edges
    print("EO of L6E start")
    EOsolution = []
    cube1.reset()
    #print("scramble:", (scr))
    cube1.doalg(scr + EOsolution)
    cube1.virtualcube()
    # print("the scramble:")
    # cube1.virtualcube()
    def count_oriented_edges(position_list):
        oriented_L6E = [24, 25, 26, 27, 44, 46]
        count = 0
        for edge in oriented_L6E:
            if position_list[edge] in oriented_L6E:
                count += 1
        return count

    if cube1.M_rotations % 2 != 0:
        cube1.doalg(["Mi"])
        EOsolution += ["Mi"]
    oriented_edges_count = count_oriented_edges(cube1.cp)
    print("oriented edges:", oriented_edges_count, "M_rotations:", cube1.M_rotations)

    breakvariable = False

    if oriented_edges_count == 6:
        breakvariable = True

    while True:
        sp = cube1.cp

        for auf in [[""], ["U"], ["Ui"], ["U2"]]:
            if not breakvariable:
                for eoalg in l6e_group:
                    #for alg in alg_list(eoalg):
                    cube1.doalg(auf + eoalg)
                    #print(auf + eoalg, count_oriented_edges(cube1.cp))
                    if count_oriented_edges(cube1.cp) == 6:
                        EOsolution += auf + eoalg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
            if breakvariable: break
        if breakvariable: break


    EOsolution = [elem for elem in EOsolution if elem != ""]
    cube1.virtualcube()
    #print("end of EOsolution")
    return EOsolution

def solveROUXlredges(scr):  # solve positions 25 and 27
    lredges_solution = []
    cube1.reset()
    #print("scramble:", (scr))
    cube1.doalg(scr + lredges_solution)
    print("LREDGES")
    spo = cube1.cp

    lredges = [25, 27]
    """ def are_lredges_solved(position_list):
        if all(elem == position_list[elem] for elem in lredges):
            return True
        return False"""

    def are_lredges_parallel(position_list):
        return [position_list.index(25), position_list.index(27)] in [[25, 27], [27, 25], [26, 24], [24, 26], [44, 46], [46, 44]]


    print("are the lredges parallel?", are_lredges_parallel(cube1.cp), cube1.cp.index(25), cube1.cp.index(27))

    lrpositions = [cube1.cp.index(25), cube1.cp.index(27)]

    if are_lredges_parallel(cube1.cp):
        print("lredges already parallel")
        while True:
            print("*", end="")
            sp = cube1.cp
            random_alg = random.choice([[""], ["U"]])
            random_alg += random.choice([[""], ["M2"]])
            random_alg += random.choice([["U"], ["Ui"], [""], ["U2"]]) + ["M2"]
            random_alg += random.choice([["U"], ["Ui"], [""], ["U2"]])
            cube1.doalg(random_alg)
            if all(cube1.cp[elem] == elem for elem in [25, 27, 0]):
                lredges_solution += random_alg
                print(random_alg)
                print(lredges_solution)
                cube1.virtualcube()
                break
            else:
                cube1.cp = sp
    else:
        while True: # make them parallel
            random_alg = random.choice([[""], ["M2"], ["U", "M2"]])
            cube1.doalg(random_alg)

            if are_lredges_parallel(cube1.cp):
                lredges_solution += random_alg
                print(random_alg, "this was added....")
                break

            elif any(elem in [46, 44] for elem in [cube1.cp.index(25), cube1.cp.index(27)]):
                lredges_solution += random_alg
                print(random_alg, "this was added....")
                print("one in white layer")
                sp2 = cube1.cp
                while True:
                    random_alg2 = random.choice([[""], ["U"], ["U2"], ["Ui"]])
                    random_alg2 += random.choice([["Mi"], ["M"]]) + ["U2"]
                    random_alg2 += random.choice([["Mi"], ["M"]])
                    cube1.doalg(random_alg2)
                    if are_lredges_parallel(cube1.cp):
                        lredges_solution += random_alg2
                        print(random_alg, "this was added")
                        print("both are parallel in white layer probably")
                        break
                    else:
                        cube1.cp = sp2
                break
            else:
                cube1.cp = spo

        while True:
            print("*", end="")
            sp = cube1.cp
            random_alg = random.choice([[""], ["U"]])
            random_alg += random.choice([[""], ["M2"]])
            random_alg += random.choice([["U"], ["Ui"], [""], ["U2"]]) + ["M2"]
            random_alg += random.choice([["U"], ["Ui"], [""], ["U2"]])
            cube1.doalg(random_alg)
            if all(cube1.cp[elem] == elem for elem in [25, 27, 0]):
                lredges_solution += random_alg
                print(random_alg, "this was added")
                cube1.virtualcube()
                break
            else:
                cube1.cp = sp



    lredges_solution = [elem for elem in lredges_solution if elem != ""]
    print("lredges_solution", lredges_solution)
    # print(cross_solution)
    # print(len(cross_solution))
    cube1.virtualcube()
    return lredges_solution

def solveROUXcycles(scr):  # Last Cycles
    sp = cube1.cp
    cube1.reset()
    cube1.doalg(scr)
    cycles_solution = []
    print("Last_step, Cycles")


    def count_solved_pieces(position_list):
        count = 0
        return sum(position_list[elem] == elem for elem in position_list)

    print("solved pieces count:", count_solved_pieces(cube1.cp))

    def is_cube_solved(position_list):
        if all(elem == position_list[elem] for elem in [26, 24, 44, 46, 27, 0]) and cube1.M_rotations % 4 == 0:
            return True
        return False

    if is_cube_solved(cube1.cp):
        print("cube already solved")
    else:
        while True:
            print("^", end="")
            random_alg = random.choice([["M"], ["Mi"], ["M2"], [""]])
            random_alg += random.choice([[""], ["U2"]])
            random_alg += random.choice([["M"], ["Mi"], ["M2"], [""]])
            random_alg += random.choice([[""], ["U2"]])
            random_alg += random.choice([["M"], ["Mi"], [""], ["M2"]])
            cube1.doalg(random_alg)
            if is_cube_solved(cube1.cp):
                cycles_solution += random_alg
                print(random_alg)
                cube1.virtualcube()
                break
            else:
                cube1.cp = sp




    cycles_solution = [elem for elem in cycles_solution if elem != ""]
    print("cycles_solution", cycles_solution)
    # print(cross_solution)
    # print(len(cross_solution))
    # cube1.virtualcube()
    return cycles_solution

def solveROUX(scr, print_solution = False):
    ROUXsolution = []
    if print_solution:
        cube1.reset().doalg(scr).virtualcube().reset()
    ROUXsolution += [" | "] + solveROUXbase(scr)
    ROUXsolution += [" | "] + solveROUXblocks(scr + ROUXsolution)
    ROUXsolution += [" | "] + solveROUXcmll(scr + ROUXsolution)
    ROUXsolution += [" | "] + solveROUXEO(scr + ROUXsolution)
    ROUXsolution += [" | "] + solveROUXlredges(scr + ROUXsolution)
    ROUXsolution += [" | "] + solveROUXcycles(scr + ROUXsolution)

    """
    cube1.reset()
    cube1.doalg(ROUXsolution)
    cube1.virtualcube()
    """


    if print_solution:
        cube1.virtualcube()
        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)[0]}"
            f"\nThe \033[0;34m{spell_alg(ROUXsolution)[1]}\033[0m-move solution with"
            f" \033[0;34m{spell_alg(ROUXsolution)[2]}\033[0m cube rotations is: {spell_alg(ROUXsolution)[0]}\n")





        print("-" * 143)

    #data = spell_alg(ROUXsolution, short_version=True)
    #data = CFOPsolution
    return ROUXsolution


solveROUX(scramble(20), True)


"""
#with open("solves_data/scrambles_list.txt", "r") as file:
    lines = file.readlines()

all_scrambles = []
for line in lines:
    all_scrambles.append(eval(line.strip()))

with open("solves_data/ROUX_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveROUX(scr, False)))+"\n")

"""