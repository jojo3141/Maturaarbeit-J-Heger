from Rubiks_Cube import *

def solveCFCEcross(scr):
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

def solveCFCEF2L(scr):
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

def solveCFCECLL(scr):
    CLLsolution = []
    cube1.reset()
    cube1.doalg(scr + CLLsolution)
    yellow_corners = yellow_side & corners_set
    yellow_corner_count = sum(cube1.cp[elem] in yellow_corners for elem in yellow_corners)

    def is_cll_solved(position_list):
        for num in [0, 1, 2, 3, 45, 47]:
            if position_list[num] != num:
                return False
        return True

    def before_AUF(position_list):
        sp = position_list
        for turn in ["U", "Ui", "U2", ""]:
            cube1.doalg([turn])
            if is_cll_solved(cube1.cp):
                cube1.cp = sp
                return [turn]
            cube1.cp = sp


    if not before_AUF(cube1.cp):
        while True:
            if yellow_corner_count == 1:
                sp = cube1.cp
                breakvariable = False
                for cll in cll_group1:
                    for auf2 in [[""], ["U"], ["Ui"], ["U2"]]:
                        cube1.doalg(auf2 + cll)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            CLLsolution += auf2 + cll
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable:
                        break

            elif yellow_corner_count in [0, 4]:
                sp = cube1.cp
                breakvariable = False
                for cll in cll_group2:
                    for auf2 in [[""], ["U"], ["Ui"], ["U2"]]:
                        cube1.doalg(auf2 + cll)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            CLLsolution += auf2 + cll
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable:
                        break

            elif yellow_corner_count == 2:
                sp = cube1.cp
                breakvariable = False
                for cll in cll_group3:
                    for auf2 in [[""], ["U"], ["Ui"], ["U2"]]:
                        cube1.doalg(auf2 + cll)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            CLLsolution += auf2 + cll
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable:
                        break
            if not before_AUF(cube1.cp):
                cube1.doalg(["U"])
                CLLsolution += ["U"]
            else:
                break
    CLLsolution = [elem for elem in CLLsolution if elem != ""]
    return CLLsolution

def solveCFCEELL(scr):
    ELLsolution = []
    cube1.reset()
    cube1.doalg(scr + ELLsolution)
    if not all(elem == cube1.cp[elem] for elem in [0, 24, 25, 26]) and cube1.M_rotations % 4 == 0:
        sp = cube1.cp
        breakvariable = False
        for ell in ell_group:
            for auf in [[""], ["U"], ["Ui"], ["U2"]]:
                for auf2 in [[""], ["U"], ["Ui"], ["U2"]]:
                    cube1.doalg(auf + ell + auf2)
                    if all(elem == cube1.cp[elem] for elem in [0, 24, 25, 26]) and cube1.M_rotations % 4 == 0:
                        ELLsolution += auf + ell + auf2
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp

                if breakvariable:
                    break
            if breakvariable:
                break
    ELLsolution = [elem for elem in ELLsolution if elem != ""]
    return ELLsolution

def solveCFCE(scr, print_solution = False):
    CFCEsolution = []
    if print_solution:
        cube1.reset().doalg(scr + CFCEsolution).virtualcube().reset()
    CFCEsolution += [" | "] + solveCFCEcross(scr)
    if print_solution:
        cube1.reset().doalg(scr + CFCEsolution).virtualcube().reset()
    CFCEsolution += [" | "] + solveCFCEF2L(scr + CFCEsolution)
    if print_solution:
        cube1.reset().doalg(scr + CFCEsolution).virtualcube().reset()
    CFCEsolution += [" | "] + solveCFCECLL(scr + CFCEsolution)
    if print_solution:
        cube1.reset().doalg(scr + CFCEsolution).virtualcube().reset()
    CFCEsolution += [" | "] + solveCFCEELL(scr + CFCEsolution)
    if print_solution:
        cube1.virtualcube()
        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)[0]}"
            f"\nThe \033[0;34m{spell_alg(CFCEsolution)[1]}\033[0m-move solution with"
            f" \033[0;34m{spell_alg(CFCEsolution)[2]}\033[0m cube rotations is: {spell_alg(CFCEsolution)[0]}\n")
        print("-" * 143)
    data = spell_alg(CFCEsolution, short_version=True)
    return data





solveCFCE(scramble(30), True)


