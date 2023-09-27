from Rubiks_Cube import *

def solveCFOPcross(scr):
    cross_solution = []
    cube1.reset()
    cube1.doalg(scr + cross_solution)
    white_edges_positions = list(white_side & edges_set)

    for i in range(4):
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
                        cross_solution += random_alg
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
                        cross_solution += random_alg
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
                        cross_solution += random_alg
                        break
                    else:
                        cube1.cp = sp

            if position not in white_layer | yellow_layer:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["D", "Di", "D2", ""])
                    random_alg += scramble(1, ["R", "L", "B", "F", "Ri", "Li", "Bi", "Fi"])
                    random_alg += reverse_alg(random_alg[0:1])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
                        cross_solution += random_alg
                        break
                    else:
                        cube1.cp = sp

            if position in white_side:
                while True:
                    sp = cube1.cp
                    random_alg = scramble(1, ["R", "L", "B", "F"])
                    random_alg += scramble(1, ["D", "Di", "D2", ""])
                    random_alg += reverse_alg(random_alg[0:1])
                    random_alg += reverse_alg(random_alg[1:2])
                    cube1.doalg(random_alg)
                    if cube1.cp[white_edges_positions[i]] == white_edges_positions[i]:
                        cross_solution += random_alg
                        break
                    else:
                        cube1.cp = sp

    cross_solution = [elem for elem in cross_solution if elem != ""]
    return cross_solution

def solveCFOPF2L(scr):
    F2L_solution = []
    cube1.reset().doalg(scr)

    pair1 = (6, 11, 20, 29, 35)
    pair2 = (10, 14, 21, 33, 39)
    pair3 = (19, 7, 22, 41, 31)
    pair4 = (15, 18, 23, 37, 43)

    not_solved_pairs = [pair1, pair2, pair3, pair4]
    not_solved_pairs = [pair for pair in not_solved_pairs if not all(cube1.is_position_solved(elem) for elem in pair)]

    def count_solved_pairs():
        solved_pairs = 4 - len([pair for pair in [pair1, pair2, pair3, pair4] if not all(cube1.is_position_solved(elem) for elem in pair)])
        return solved_pairs

    def analyse_pair_position(pair):
        sidelist = []
        for elem in pair:
            sidelist += [on_which_side(elem)]
        unique_set = set()
        sidelist = [x for x in sidelist if not (x in unique_set or unique_set.add(x))]
        return [len(sidelist) == 3, pair[0] in yellow_layer, pair[4] in yellow_layer, pair[2] in yellow_side,
                cube1.is_position_solved(pair[2]),
                on_which_side(pair[1]) == on_which_side(pair[4]) and on_which_side(pair[0]) == on_which_side(pair[3]),
                pair[2] in yellow_side and ((on_which_side(pair[1]) == on_which_side(pair[4]))^(on_which_side(pair[0]) == on_which_side(pair[3]))),
                ((pair[1] in yellow_side and pair[3] in yellow_side) or (pair[0] in yellow_side and pair[4] in yellow_side))
                and (not (opposit_side(on_which_side(pair[2])) in sidelist)) and (not (len(sidelist)==3)),
                pair[2] in yellow_side and pair[4] in [43, 31, 35, 39]]

    while len(not_solved_pairs) > 0:
        pair_positions = [[cube1.cp.index(elem) for elem in pair] for pair in not_solved_pairs]
        app_list = [analyse_pair_position(pair) for pair in pair_positions]
        starting_correct_pairs = count_solved_pairs()
        pair_changed = False
        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if (app[1] and app[2] and app[5]) or app[7]:
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if app[5]:
                    sp = cube1.cp
                    while True:
                        random_alg = pair_insertion()
                        cube1.doalg(random_alg)
                        if (cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer)\
                                and starting_correct_pairs == count_solved_pairs():
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if app[1] and app[2] and not app[6]:
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp
                    sp = cube1.cp
                    while True:
                        random_alg = []
                        random_alg += scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if app[1] ^ app[2] and not app[8]:
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp
                    sp = cube1.cp
                    while True:
                        random_alg = []
                        random_alg += scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                F2L_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if (not app[1] and not app[2]) or app[6] or app[8]:
                    sp = cube1.cp
                    while True:
                        random_alg = pair_insertion()
                        random_alg += scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if ((step_app[1] and step_app[2] and step_app[5]) or step_app[7]) and (count_solved_pairs() == starting_correct_pairs):
                                F2L_solution += random_alg
                                break
                        cube1.cp = sp
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
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
        not_solved_pairs = [pair for pair in not_solved_pairs if not all(cube1.is_position_solved(elem) for elem in pair)]

    F2L_solution = [elem for elem in F2L_solution if elem != ""]
    return F2L_solution

def solveCFOPOLL(scr):
    OLLsolution = []
    cube1.reset()
    cube1.doalg(scr + OLLsolution)
    yellow_edges = yellow_side & edges_set
    yellow_corners = yellow_side & corners_set
    yellow_edges_count = sum(cube1.cp[elem] in yellow_edges for elem in yellow_edges)
    yellow_corner_count = sum(cube1.cp[elem] in yellow_corners for elem in yellow_corners)
    count = yellow_edges_count + yellow_corner_count + 1
    if count != 9:
        minus_shape = False
        if (cube1.cp[24] in yellow_side and cube1.cp[26] in yellow_side)\
                ^(cube1.cp[25] in yellow_side and cube1.cp[27] in yellow_side):
            minus_shape = True
        if yellow_edges_count == 0 and yellow_corner_count < 2:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group1:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 2 and yellow_corner_count == 0 and not minus_shape:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group2:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 2 and yellow_corner_count == 1 and not minus_shape:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group3:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 2 and yellow_corner_count == 2 and not minus_shape:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group4:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 2 and yellow_corner_count == 0 and minus_shape:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group5:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 2 and yellow_corner_count == 1 and minus_shape:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group6:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 2 and yellow_corner_count == 2 and minus_shape:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group7:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 0:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group8:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 4 and yellow_corner_count < 2:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group9:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 4 and yellow_corner_count == 2:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group10:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break

        elif yellow_edges_count == 2 and yellow_corner_count == 4:
            sp = cube1.cp
            breakvariable = False
            for oll in oll_group11:
                for alg in alg_list(oll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] in yellow_side for elem in yellow_side) == 8:
                        OLLsolution += alg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break
    OLLsolution = [elem for elem in OLLsolution if elem != ""]
    return OLLsolution

def solveCFOPPLL(scr):
    PLLsolution = []
    cube1.reset()
    cube1.doalg(scr + PLLsolution)
    correct_yellow_pieces = sum(cube1.cp[elem] == elem for elem in yellow_side)
    if correct_yellow_pieces != 8:
        if True:
            sp = cube1.cp
            breakvariable = False
            for pll in pll_group:
                for alg in alg_list(pll):
                    cube1.doalg(alg)
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        PLLsolution += alg
                        breakvariable = True
                        break
                    cube1.doalg("U")
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        PLLsolution += alg + ["U"]
                        breakvariable = True
                        break
                    cube1.doalg("U")
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        PLLsolution += alg + ["U2"]
                        breakvariable = True
                        break
                    cube1.doalg("U")
                    if sum(cube1.cp[elem] == elem for elem in yellow_side) == 8:
                        PLLsolution += alg + ["Ui"]
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
                if breakvariable:
                    break
    PLLsolution = [elem for elem in PLLsolution if elem != ""]
    return PLLsolution


def solveCFOP(scr, print_solution = False):
    CFOPsolution = []
    if print_solution:
        cube1.reset().doalg(scr + CFOPsolution).virtualcube().reset()
    CFOPsolution += [" | "] + solveCFOPcross(scr)
    if print_solution:
        cube1.reset().doalg(scr + CFOPsolution).virtualcube().reset()
    CFOPsolution += [" | "] + solveCFOPF2L(scr + CFOPsolution)
    if print_solution:
        cube1.reset().doalg(scr + CFOPsolution).virtualcube().reset()
    CFOPsolution += [" | "] + solveCFOPOLL(scr + CFOPsolution)
    if print_solution:
        cube1.reset().doalg(scr + CFOPsolution).virtualcube().reset()
    CFOPsolution += [" | "] + solveCFOPPLL(scr + CFOPsolution)
    if print_solution:
        cube1.virtualcube()
        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)[0]}"
            f"\nThe \033[0;34m{spell_alg(CFOPsolution)[1]}\033[0m-move solution with"
            f" \033[0;34m{spell_alg(CFOPsolution)[2]}\033[0m cube rotations is: {spell_alg(CFOPsolution)[0]}\n")
        print("-" * 143)
    data = spell_alg(CFOPsolution, short_version=True)
    return data



solveCFOP(scramble(30), True) # Eine zuffällige Konfiguration wird gelöst



# Die 10000 zuvor bestimmten zufälligen Konfigurationen werden gelöst
with open("scrambles_list.txt", "r") as file:
    lines = file.readlines()

all_scrambles = []
for line in lines:
    all_scrambles.append(eval(line.strip()))


with open("CFCE_solutions.txt", "w") as file:
    for scr in all_scrambles:
        file.write((str(solveCFOP(scr, False)))+"\n")