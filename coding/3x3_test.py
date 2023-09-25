import random


#All solved positions
original_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]


#Definitions for U/F/R/L/D/B-turns
def U_turn(list):
	return [list[1], list[2], list[3], list[0], list[16], list[17], list[6], list[7], list[4], list[5], list[10], list[11],
            list[8], list[9], list[14], list[15], list[12], list[13], list[18], list[19], list[20], list[21], list[22], list[23],
            list[25], list[26], list[27], list[24], list[40], list[29], list[30], list[31], list[28], list[33], list[34], list[35],
            list[32], list[37], list[38], list[39], list[36], list[41], list[42], list[43], list[44], list[45], list[46], list[47]]
def F_turn(list):
	return [list[0], list[1], list[15], list[12], list[4], list[2], list[3], list[7], list[9], list[10], list[11], list[8],
            list[21], list[13], list[14], list[20], list[16], list[17], list[18], list[19], list[5], list[6], list[22], list[23],
            list[24], list[25], list[39], list[27], list[28], list[26], list[30], list[31], list[33], list[34], list[35], list[32],
            list[36], list[37], list[38], list[44], list[40], list[41], list[42], list[43], list[29], list[45], list[46], list[47]]
def R_turn(list):
	return [list[0], list[19], list[16], list[3], list[4], list[5], list[6], list[7], list[8], list[1], list[2], list[11],
            list[13], list[14], list[15], list[12], list[22], list[17], list[18], list[21], list[20], list[9], list[10], list[23],
            list[24], list[43], list[26], list[27], list[28], list[29], list[30], list[31], list[32], list[25], list[34], list[35],
            list[37], list[38], list[39], list[36], list[40], list[41], list[42], list[45], list[44], list[33], list[46], list[47]]
def L_turn(list):
	return [list[8], list[1], list[2], list[11], list[5], list[6], list[7], list[4], list[20], list[9], list[10], list[23],
            list[12], list[13], list[14], list[15], list[16], list[3], list[0], list[19], list[18], list[21], list[22], list[17],
            list[24], list[25], list[26], list[35], list[29], list[30], list[31], list[28], list[32], list[33], list[34], list[47],
            list[36], list[37], list[38], list[39], list[40], list[27], list[42], list[43], list[44], list[45], list[46], list[41]]
def D_turn(list):
	return [list[0], list[1], list[2], list[3], list[4], list[5], list[10], list[11], list[8], list[9], list[14], list[15],
            list[12], list[13], list[18], list[19], list[16], list[17], list[6], list[7], list[21], list[22], list[23], list[20],
            list[24], list[25], list[26], list[27], list[28], list[29], list[34], list[31], list[32], list[33], list[38], list[35],
            list[36], list[37], list[42], list[39], list[40], list[41], list[30], list[43], list[45], list[46], list[47], list[44]]
def B_turn(list):
	return [list[7], list[4], list[2], list[3], list[23], list[5], list[6], list[22], list[8], list[9], list[10], list[11],
            list[12], list[0], list[1], list[15], list[17], list[18], list[19], list[16], list[20], list[21], list[13], list[14],
            list[31], list[25], list[26], list[27], list[28], list[29], list[30], list[46], list[32], list[33], list[34], list[35],
            list[36], list[24], list[38], list[39], list[41], list[42], list[43], list[40], list[44], list[45], list[37], list[47]]



#Definitions of inverted turns
def Ui_turn(list):
    return [list[3], list[0], list[1], list[2], list[8], list[9], list[6], list[7], list[12], list[13], list[10], list[11],
            list[16], list[17], list[14], list[15], list[4], list[5], list[18], list[19], list[20], list[21], list[22], list[23],
            list[27], list[24], list[25], list[26], list[32], list[29], list[30], list[31], list[36], list[33], list[34], list[35],
            list[40], list[37], list[38], list[39], list[28], list[41], list[42], list[43], list[44], list[45], list[46], list[47]]
def Fi_turn(list):
    return [list[0], list[1], list[5], list[6], list[4], list[20], list[21], list[7], list[11], list[8], list[9], list[10],
            list[3], list[13], list[14], list[2], list[16], list[17], list[18], list[19], list[15], list[12], list[22], list[23],
            list[24], list[25], list[29], list[27], list[28], list[44], list[30], list[31], list[35], list[32], list[33], list[34],
            list[36], list[37], list[38], list[26], list[40], list[41], list[42], list[43], list[39], list[45], list[46], list[47]]
def Ri_turn(list):
    return [list[0], list[9], list[10], list[3], list[4], list[5], list[6], list[7], list[8], list[21], list[22], list[11],
            list[15], list[12], list[13], list[14], list[2], list[17], list[18], list[1], list[20], list[19], list[16], list[23],
            list[24], list[33], list[26], list[27], list[28], list[29], list[30], list[31], list[32], list[45], list[34], list[35],
            list[39], list[36], list[37], list[38], list[40], list[41], list[42], list[25], list[44], list[43], list[46], list[47]]
def Li_turn(list):
    return [list[18], list[1], list[2], list[17], list[7], list[4], list[5], list[6], list[0], list[9], list[10], list[3],
            list[12], list[13], list[14], list[15], list[16], list[23], list[20], list[19], list[8], list[21], list[22], list[11],
            list[24], list[25], list[26], list[41], list[31], list[28], list[29], list[30], list[32], list[33], list[34], list[27],
            list[36], list[37], list[38], list[39], list[40], list[47], list[42], list[43], list[44], list[45], list[46], list[35]]
def Di_turn(list):
    return [list[0], list[1], list[2], list[3], list[4], list[5], list[18], list[19], list[8], list[9], list[6], list[7],
            list[12], list[13], list[10], list[11], list[16], list[17], list[14], list[15], list[23], list[20], list[21], list[22],
            list[24], list[25], list[26], list[27], list[28], list[29], list[42], list[31], list[32], list[33], list[30], list[35],
            list[36], list[37], list[34], list[39], list[40], list[41], list[38], list[43], list[47], list[44], list[45], list[46]]
def Bi_turn(list):
    return [list[13], list[14], list[2], list[3], list[1], list[5], list[6], list[0], list[8], list[9], list[10], list[11],
            list[12], list[22], list[23], list[15], list[19], list[16], list[17], list[18], list[20], list[21], list[7], list[4],
            list[37], list[25], list[26], list[27], list[28], list[29], list[30], list[24], list[32], list[33], list[34], list[35],
            list[36], list[46], list[38], list[39], list[43], list[40], list[41], list[42], list[44], list[45], list[31], list[47]]

normal_moves = [U_turn, F_turn, R_turn, L_turn, D_turn, B_turn]
inverted_moves = [Ui_turn, Fi_turn, Ri_turn, Li_turn, Di_turn, Bi_turn]
normal_moves_short = ["U", "F", "R", "L", "D", "B"]
inverted_moves_short = ["U'", "F'", "R'", "L'", "D'", "B'"]
long_notation_names = [move.__name__ for move in normal_moves + inverted_moves]
short_notation_names = normal_moves_short + inverted_moves_short
list_of_possible_moves = normal_moves + inverted_moves
list_of_probabilities = [1, 6, 27, 12, 2256, 8969, 33058, 114149, 360508, 930588, 1350852, 782536, 90280, 276]





#Definitions to do, reverse or correct algs
def do_alg(current_positions, list_of_moves):
    print("This is the starting position:", current_positions)
    for turn in list_of_moves:
        current_positions = turn(current_positions)
    print("The alg is done, the position is now:", current_positions)
    return current_positions
def do_alg_silent(current_positions, list_of_moves):
    for move in list_of_moves:
        current_positions = move(current_positions)
    return current_positions
def reverse_alg(alg):
    alg = list(reversed(alg))                      #read the alg backwards

    for i in range(6):                             #every inverted turn gets normal and vice versa
        for j in range(len(alg)):
            if alg[j] == normal_moves[i]:
                alg[j] = inverted_moves[i]
            elif alg[j] == inverted_moves[i]:
                alg[j] = normal_moves[i]
    return alg
def correct_alg(alg): #this only kicks out normal moves followed by inverted and vice versa, not triple moves nor F-B'...

    for i in range(len(alg)//2):

        for i in range(len(alg) - 1):

            for j in range(6):
                if alg[i] == normal_moves[j].__name__ and alg[i + 1] == inverted_moves[j].__name__:
                    del alg[i:i + 2]
                    break
            else:
                continue
            break
        for i in range(len(alg) - 1):
            for j in range(6):
                if alg[i] == inverted_moves[j].__name__ and alg[i + 1] == normal_moves[j].__name__:
                    del alg[i:i + 2]
                    break
            else:
                continue
            break

    return alg
def spell_alg(alg):
    alg = [move.__name__ for move in alg]
    for i in range(12):
        for j in range(len(alg)):
            if alg[j] == long_notation_names[i]:
                alg[j] = short_notation_names[i]

    new_list = []
    for element in alg:
        new_list.append(element + " ")
    string_alg = "".join(new_list)
    return string_alg



#Definitions for solving method
def solve_with_number(scramble, number_of_turns, attemps, count=0):
    scrambled_positions = do_alg_silent(original_positions, scramble)

    for attemp in range(attemps):
        random_move_list = [random.choice(list_of_possible_moves) for i in range(number_of_turns)]
        if scrambled_positions in [do_alg_silent(original_positions, random_move_list)]:

            print(f"I found a \033[1;35m{len(correct_alg([move.__name__ for move in reverse_alg(random_move_list)]))}"
                  f" move solution\033[0m:", correct_alg([move.__name__ for move in reverse_alg(random_move_list)]))
            print("The scramble was:", [move.__name__ for move in scramble])
            print(f"I needed {attemp+1} additional attemps")
            return True
def try_to_solve(scramble):
    total_attempts = 0
    for i in range(15):                                                            #gods number is 14 + solved position
        total_attempts += list_of_probabilities[i]
        print(f"I calculated \033[1;35m{i}\033[0m moves max attempts: \033[1;35m{total_attempts} \033[0m")
        if solve_with_number(scramble, i, list_of_probabilities[i]) == True:       #It doesn't try to find the
            return True                                                   #perfect solution
def solve_until_solution_found(scramble):              #Does try_to_solve until a solution is found.
    while try_to_solve(scramble) != True:
        try_to_solve(scramble)




"""hardest_scramble = [F_turn, F_turn, U_turn, F_turn, F_turn, U_turn, U_turn,
                    R_turn, R_turn, U_turn, R_turn, R_turn, U_turn]

easy_scramble = [Ri_turn, Ui_turn, Ri_turn, L_turn, Di_turn, R_turn, R_turn, Di_turn, Li_turn]

random_scramble = [random.choice(list_of_possible_moves) for i in range(4)]

solve_until_solution_found(random_scramble)"""



def scramble(number_of_turns):
    return [random.choice(list_of_possible_moves) for _ in range(number_of_turns)]

def check_common_elements(list1, list2):
    common_elements = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            common_elements += 1
    #print("The lists have", common_elements, "elements in common.")
    return common_elements


def try_five_moves(starting_position, number_of_correct_elements=0):
    starting_number_of_correct_elements = number_of_correct_elements
    for i in range(100000):
        random_move_list = [random.choice(list_of_possible_moves) for _ in range(5)]
        if check_common_elements(original_positions, do_alg_silent(starting_position, random_move_list))>number_of_correct_elements:
            number_of_correct_elements = check_common_elements(original_positions, do_alg_silent(starting_position, random_move_list))
            best_five_moves = random_move_list
            #print(f"wrong_attempts = {wrong_attempts}")
            #print(f"\033[1;35m{number_of_correct_elements} correct elements\033[0m, best moves were: {[move.__name__ for move in best_five_moves]}")
            if number_of_correct_elements == 48:
                break
        else:
            if starting_number_of_correct_elements == number_of_correct_elements:
                best_five_moves = []

    return [best_five_moves, number_of_correct_elements]






def improve_cube(scramble):
    print(f"\033[1;35mthe scramble was:\033[34m {spell_alg(scramble)}\033[0m")
    unsuccessful_attempts = 0
    while True:
        scrambled_position = do_alg_silent(original_positions, scramble)
        number_of_correct_elements = check_common_elements(original_positions, scrambled_position)
        results = try_five_moves(scrambled_position, number_of_correct_elements)
        best_five_moves, number_of_correct_elements = results[0], results[1]
        print(f"and the best five moves were:    \033[32m{spell_alg(best_five_moves)}\033[0m", end="    ")
        print(f"There are now \033[1;35m{number_of_correct_elements} correct elements\033[0m")
        scramble += best_five_moves
        if best_five_moves == []:
            unsuccessful_attempts += 1
            max_unsuccessful_attempts = 5
            if unsuccessful_attempts == max_unsuccessful_attempts:
                print(f"I had {max_unsuccessful_attempts} unsuccessful attempts :(")
                print(f"\033[32m{check_common_elements(original_positions, do_alg_silent(original_positions, scramble))}\033[0m")
                print(spell_alg(scramble))
                break
        if number_of_correct_elements == 48:
            print(f"\033[32m{do_alg_silent(original_positions, scramble)}\033[0m")
            break




#improve_cube(scramble(5))

#L' R F L U' U R' F' F U' =>38
#t2 = [D_turn, R_turn, Li_turn, Fi_turn, Ri_turn, L_turn]

testalg = [Li_turn, R_turn, F_turn, L_turn, Ui_turn, U_turn, Ri_turn, Fi_turn, F_turn, Ui_turn, U_turn, Di_turn]
testalg2 = [Li_turn, R_turn, F_turn, L_turn, Ri_turn, Di_turn]

def mark_equal_elements_of_two_lists(compare_list, list):
    print("\t[", end="")
    for i in range(48):
        if compare_list[i] == list[i]:
            if i == 47:
                print(f"\033[31m{list[i]}\033[0m]")
            else:
                print(f"\033[31m{list[i]}\033[0m, ", end="")
        else:
            if i == 47:
                print(f"{list[i]}]")
            else:
                print(f"{list[i]}, ", end="")
def mark_changes_between_two_lists(compare_list, list):
    print("[", end="")
    for i in range(48):
        if compare_list[i] != list[i]:
            if i == 47:
                print(f"\033[36m{list[i]}\033[0m]")
            else:
                print(f"\033[36m{list[i]}\033[0m, ", end="")
        else:
            if i == 47:
                print(f"{list[i]}]")
            else:
                print(f"{list[i]}, ", end="")
def see_what_happens(alg):
    print(f"Calculated correct elements = {check_common_elements((do_alg_silent(original_positions, alg)), original_positions)}")
    print(spell_alg(alg))

    print(f"0 =\t{original_positions}")
    current_positions = original_positions
    for i in range(len(alg)):
        print(spell_alg([alg[i]]), end="\t")
        mark_changes_between_two_lists(current_positions, do_alg_silent(current_positions, [alg[i]]))
        #print(f"{spell_alg([alg[i]])}\t{do_alg_silent(current_positions, [alg[i]])}")
        current_positions = do_alg_silent(current_positions, [alg[i]])

    mark_equal_elements_of_two_lists(original_positions, current_positions)





see_what_happens(testalg2)


