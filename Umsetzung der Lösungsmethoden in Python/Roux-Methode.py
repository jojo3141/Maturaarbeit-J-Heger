from Rubiks_Cube import *


def solveROUXbase(scr):
    base_solution = []
    cube1.reset()
    cube1.doalg(scr + base_solution)
    white_edges_positions = [47, 45]

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
                        base_solution += random_alg
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
                        base_solution += random_alg
                        break
                    else:
                        cube1.cp = sp

    base_solution = [elem for elem in base_solution if elem != ""]
    return base_solution

def solveROUXblocks(scr):
    block_solution = []
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
                pair[2] in yellow_side and pair[4] in [43, 31, 35, 39], pair[4] in white_layer or pair [3] in white_layer]

    while len(not_solved_pairs) > 0:
        pair_positions = [[cube1.cp.index(elem) for elem in pair] for pair in not_solved_pairs]
        app_list = [analyse_pair_position(pair) for pair in pair_positions]
        starting_correct_pairs = count_solved_pairs()
        just_a_M_turn = False
        pair_changed = False
        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if ((app[1] and app[2] and app[5]) or app[7]) and not app[9]:
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if app[5] and not app[9]:
                    sp = cube1.cp
                    while True:
                        random_alg = pair_insertion()
                        cube1.doalg(random_alg)
                        if (cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer)\
                                and starting_correct_pairs == count_solved_pairs():
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                block_solution += random_alg
                                break
                        cube1.cp = sp

                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if (app[1] and app[2] and not app[6]) and not app[9]:
                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                block_solution += random_alg
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
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if (app[1] ^ app[2] and not app[8]) and not app[9]:
                    sp = cube1.cp

                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += extended_pair_insertion()
                        cube1.doalg(random_alg)
                        if cube1.cp.index(pair[0]) in yellow_layer and cube1.cp.index(pair[4]) in yellow_layer\
                                and starting_correct_pairs == count_solved_pairs():
                            step_app = analyse_pair_position([cube1.cp.index(elem) for elem in pair])
                            if (step_app[1] and step_app[2] and step_app[5]) or step_app[7]:
                                block_solution += random_alg
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
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if ((not app[1] and not app[2]) or app[6] or app[8]) and not app[9]:
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
                                block_solution += random_alg
                                break
                        cube1.cp = sp

                    sp = cube1.cp
                    while True:
                        random_alg = scramble(1, ["U", "Ui", "U2", ""])
                        random_alg += pair_insertion()
                        cube1.doalg(random_alg)
                        if all(cube1.is_position_solved(elem) for elem in pair):
                            if count_solved_pairs() > starting_correct_pairs:
                                block_solution += random_alg
                                pair_changed = True
                                break
                        else:
                            cube1.cp = sp
                    break

        if pair_changed == False:
            for app, pair in zip(app_list, not_solved_pairs):
                if app[9]:
                    if cube1.cp.index(pair[4]) in [34, 44]:
                        cube1.doalg(["Mi"])
                        block_solution += ["Mi"]
                    elif cube1.cp.index(pair[4]) in [42, 46]:
                        cube1.doalg(["M"])
                        block_solution += ["M"]
                    pair_changed = True
                    just_a_M_turn = True



        if not just_a_M_turn:
            block_solution += [" | "]
        not_solved_pairs = [pair for pair in not_solved_pairs if not all(cube1.is_position_solved(elem) for elem in pair)]

    block_solution = [elem for elem in block_solution if elem != ""]
    return block_solution

def solveROUXcmll(scr):
    CMLLsolution = []
    cube1.reset()
    cube1.doalg(scr + CMLLsolution)
    yellow_corners = yellow_side & corners_set
    yellow_corner_count = sum(cube1.cp[elem] in yellow_corners for elem in yellow_corners)

    def is_cmll_solved(position_list):
        for num in [0, 1, 2, 3, 45, 47]:
            if position_list[num] != num:
                return False
        return True

    def before_AUF(position_list):
        sp = position_list
        for turn in ["U", "Ui", "U2", ""]:
            cube1.doalg([turn])
            if is_cmll_solved(cube1.cp):
                cube1.cp = sp
                return [turn]
            cube1.cp = sp


    if not before_AUF(cube1.cp):
        while True:
            if yellow_corner_count == 1:
                sp = cube1.cp
                breakvariable = False
                for cmll in cmll_group1:
                    for alg in alg_list(cmll):
                        cube1.doalg(alg)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            CMLLsolution += alg
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable: break
            elif yellow_corner_count in [0, 4]:
                sp = cube1.cp
                breakvariable = False
                for cmll in cmll_group2:
                    for alg in alg_list(cmll):
                        cube1.doalg(alg)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            CMLLsolution += alg
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable: break

            elif yellow_corner_count == 2:
                sp = cube1.cp
                breakvariable = False
                for cmll in cmll_group3:
                    for alg in alg_list(cmll):
                        cube1.doalg(alg)
                        auf = before_AUF(cube1.cp)
                        if auf != None:
                            CMLLsolution += alg
                            breakvariable = True
                            break
                        else:
                            cube1.cp = sp
                    if breakvariable:
                        break

            if not before_AUF(cube1.cp):
                cube1.doalg(["U"])
                CMLLsolution += ["U"]
            else:
                break


    CMLLsolution = [elem for elem in CMLLsolution if elem != ""]
    return CMLLsolution

def solveROUXEO(scr):
    EOsolution = []
    cube1.reset()
    cube1.doalg(scr + EOsolution)
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
    breakvariable = False

    if oriented_edges_count == 6:
        breakvariable = True

    while True:
        sp = cube1.cp
        for auf in [[""], ["U"], ["Ui"], ["U2"]]:
            if not breakvariable:
                for eoalg in l6e_group:
                    cube1.doalg(auf + eoalg)
                    if count_oriented_edges(cube1.cp) == 6:
                        EOsolution += auf + eoalg
                        breakvariable = True
                        break
                    else:
                        cube1.cp = sp
            if breakvariable:
                break
        if breakvariable:
            break


    EOsolution = [elem for elem in EOsolution if elem != ""]
    return EOsolution

def solveROUXlredges(scr):
    lredges_solution = []
    cube1.reset()
    cube1.doalg(scr + lredges_solution)
    spo = cube1.cp

    def are_lredges_parallel(position_list):
        return [position_list.index(25), position_list.index(27)] in [[25, 27], [27, 25], [26, 24], [24, 26], [44, 46], [46, 44]]


    if are_lredges_parallel(cube1.cp):
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
                break
            else:
                cube1.cp = sp
    else:
        while True:
            random_alg = random.choice([[""], ["M2"], ["U", "M2"]])
            cube1.doalg(random_alg)
            if are_lredges_parallel(cube1.cp):
                lredges_solution += random_alg
                break

            elif any(elem in [46, 44] for elem in [cube1.cp.index(25), cube1.cp.index(27)]):
                lredges_solution += random_alg
                sp2 = cube1.cp
                while True:
                    random_alg2 = random.choice([[""], ["U"], ["U2"], ["Ui"]])
                    random_alg2 += random.choice([["Mi"], ["M"]]) + ["U2"]
                    random_alg2 += random.choice([["Mi"], ["M"]])
                    cube1.doalg(random_alg2)
                    if are_lredges_parallel(cube1.cp):
                        lredges_solution += random_alg2
                        break
                    else:
                        cube1.cp = sp2
                break
            else:
                cube1.cp = spo

        while True:
            sp = cube1.cp
            random_alg = random.choice([[""], ["U"]])
            random_alg += random.choice([[""], ["M2"]])
            random_alg += random.choice([["U"], ["Ui"], [""], ["U2"]]) + ["M2"]
            random_alg += random.choice([["U"], ["Ui"], [""], ["U2"]])
            cube1.doalg(random_alg)
            if all(cube1.cp[elem] == elem for elem in [25, 27, 0]):
                lredges_solution += random_alg
                break
            else:
                cube1.cp = sp

    lredges_solution = [elem for elem in lredges_solution if elem != ""]
    return lredges_solution

def solveROUXcycles(scr):
    sp = cube1.cp
    cube1.reset()
    cube1.doalg(scr)
    cycles_solution = []

    def count_solved_pieces(position_list):
        count = 0
        return sum(position_list[elem] == elem for elem in position_list)

    def is_cube_solved(position_list):
        if all(elem == position_list[elem] for elem in [26, 24, 44, 46, 27, 0]) and cube1.M_rotations % 4 == 0:
            return True
        return False

    if not is_cube_solved(cube1.cp):
        while True:
            random_alg = random.choice([["M"], ["Mi"], ["M2"], [""]])
            random_alg += random.choice([[""], ["U2"]])
            random_alg += random.choice([["M"], ["Mi"], ["M2"], [""]])
            random_alg += random.choice([[""], ["U2"]])
            random_alg += random.choice([["M"], ["Mi"], [""], ["M2"]])
            cube1.doalg(random_alg)
            if is_cube_solved(cube1.cp):
                cycles_solution += random_alg
                break
            else:
                cube1.cp = sp

    cycles_solution = [elem for elem in cycles_solution if elem != ""]
    return cycles_solution

def solveROUX(scr, print_solution = False):
    ROUXsolution = []
    if print_solution:
        cube1.reset().doalg(scr + ROUXsolution).virtualcube().reset()
    ROUXsolution += [" | "] + solveROUXbase(scr)
    ROUXsolution += [" | "] + solveROUXblocks(scr + ROUXsolution)
    if print_solution:
        cube1.reset().doalg(scr + ROUXsolution).virtualcube().reset()
    ROUXsolution += [" | "] + solveROUXcmll(scr + ROUXsolution)
    if print_solution:
        cube1.reset().doalg(scr + ROUXsolution).virtualcube().reset()
    ROUXsolution += [" | "] + solveROUXEO(scr + ROUXsolution)
    ROUXsolution += [" | "] + solveROUXlredges(scr + ROUXsolution)
    ROUXsolution += [" | "] + solveROUXcycles(scr + ROUXsolution)

    if print_solution:
        cube1.virtualcube()
        print("\033[0m" + "-" * 143)
        print(
            f"The \033[0;34m{len(scr)}\033[0m-move scramble was: {spell_alg(scr)[0]}"
            f"\nThe \033[0;34m{spell_alg(ROUXsolution)[1]}\033[0m-move solution with"
            f" \033[0;34m{spell_alg(ROUXsolution)[2]}\033[0m cube rotations is: {spell_alg(ROUXsolution)[0]}\n")
        print("-" * 143)

    return ROUXsolution



solveROUX(scramble(30), True)