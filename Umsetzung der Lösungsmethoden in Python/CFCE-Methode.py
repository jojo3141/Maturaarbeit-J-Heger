
from class_Cubie import *


def solveCFCEcross(scr):
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

def solveCFCEF2L(scr):
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

def solveCFCECMLL(scr):            # ORIENTATION OF THE LAST LAYER
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
                # print([turn], "this is the auf that leads to solved")
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
                print("no matching case found", "#Problem " * 100)
                cube1.doalg(["U"])
                CMLLsolution += ["U"]
            else:
                break

    CMLLsolution = [elem for elem in CMLLsolution if elem != ""]
    print("CMLLsolution:", CMLLsolution)
    # print(len(cross_solution))
    cube1.virtualcube()
    return CMLLsolution

def solveCFCEELL(scr):
    ELLsolution = []
    cube1.reset()
    print("ELL start")
    cube1.doalg(scr + ELLsolution)

    if all(elem == cube1.cp[elem] for elem in [0, 24, 25, 26,]) and cube1.M_rotations % 4 == 0:
        print("ELL is done!")
    else:

        sp = cube1.cp
        breakvariable = False
        for ell in ell_group:
            for auf in [[""], ["U"], ["Ui"], ["U2"]]:
                for auf2 in [[""], ["U"], ["Ui"], ["U2"]]:
                    cube1.doalg(auf + ell + auf2)
                    if all(elem == cube1.cp[elem] for elem in [0, 24, 25, 26,]) and cube1.M_rotations % 4 == 0:
                        print("ELL solved with the alg:", auf + ell + auf2)
                        ELLsolution += auf + ell + auf2
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp

                if breakvariable: break
            if breakvariable: break



    ELLsolution = [elem for elem in ELLsolution if elem != ""]
    # print(cross_solution)
    # print(len(cross_solution))
    # cube1.virtualcube()
    return ELLsolution


def solveCFCE(scr, print_solution = False):
    CFCEsolution = []
    if print_solution:
        cube1.reset().doalg(scr).virtualcube().reset()
    CFCEsolution += [" | "] + solveCFCEcross(scr)
    CFCEsolution += [" | "] + solveCFCEF2L(scr + CFCEsolution)
    CFCEsolution += [" | "] + solveCFCECMLL(scr + CFCEsolution)
    CFCEsolution += [" | "] + solveCFCEELL(scr + CFCEsolution)



    if print_solution:
        cube1.virtualcube()
        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)[0]}"
            f"\nThe \033[0;34m{spell_alg(CFCEsolution)[1]}\033[0m-move solution with"
            f" \033[0;34m{spell_alg(CFCEsolution)[2]}\033[0m cube rotations is: {spell_alg(CFCEsolution)[0]}\n")


        #LBLsolutionAlg = Alg(LBLsolution)
        #LBLsolutionAlg.correct()
        #print("cancel moves out:", spell_alg(LBLsolutionAlg.alg)[1])
        #count_moves(LBLsolutionAlg.alg)

        print("-" * 143)

    data = spell_alg(CFCEsolution, short_version=True)
    return data




solveCFCE(scramble(20), True)




"""
#with open("solves_data/scrambles_list.txt", "r") as file:
    lines = file.readlines()

all_scrambles = []
for line in lines:
    all_scrambles.append(eval(line.strip()))


with open("solves_data/CFCE_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveCFCE(scr, False)))+"\n")
"""