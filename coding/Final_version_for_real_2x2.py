import random

#All solved positions
original_positions0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]#
original_positions1 = [22, 7, 20, 13, 5, 11, 0, 17, 14, 8, 4, 10, 2, 19, 15, 9, 6, 23, 12, 21, 18, 3, 16, 1]#R L'
original_positions2 = [6, 23, 12, 21, 10, 4, 16, 1, 9, 15, 11, 5, 18, 3, 8, 14, 22, 7, 20, 13, 2, 19, 0, 17]#R2 L2
original_positions3 = [16, 17, 18, 19, 11, 10, 22, 23, 15, 14, 5, 4, 20, 21, 9, 8, 0, 1, 2, 3, 12, 13, 6, 7]#R' L
original_positions4 = [17, 19, 16, 18, 13, 12, 11, 10, 22, 23, 7, 6, 5, 4, 20, 21, 2, 0, 3, 1, 14, 15, 8, 9]#F B'
original_positions5 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 23, 22, 21, 20]#F2 B2
original_positions6 = [18, 16, 19, 17, 22, 23, 15, 14, 13, 12, 20, 21, 9, 8, 7, 6, 1, 3, 0, 2, 10, 11, 4, 5]#F' B
original_positions7 = [5, 11, 4, 10, 2, 0, 20, 22, 18, 16, 3, 1, 21, 23, 19, 17, 9, 15, 8, 14, 6, 12, 7, 13]#U D'
original_positions8 = [3, 2, 1, 0, 8, 9, 21, 20, 4, 5, 14, 15, 23, 22, 10, 11, 19, 18, 17, 16, 7, 6, 13, 12]#U2 D2
original_positions9 = [14, 8, 15, 9, 17, 19, 23, 21, 1, 3, 16, 18, 22, 20, 0, 2, 10, 4, 11, 5, 13, 7, 12, 6]#U' D



#Definitions for U/F/R/L/D/B-turns
def U_turn(list):
    new_positions = [list[0], list[1], list[11], list[5], list[4], list[16], list[12], list[6],
                     list[2], list[9], list[10], list[17], list[13], list[7], list[3], list[15],
                     list[14], list[8], list[18], list[19], list[20], list[21], list[22], list[23]]
    return new_positions
def F_turn(list):
    new_positions = [list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7],
                     list[8], list[9], list[23], list[22], list[10], list[11], list[12], list[13],
                     list[18], list[16], list[19], list[17], list[20], list[21], list[15], list[14]]
    return new_positions
def R_turn(list):
    new_positions = [list[0], list[7], list[2], list[13], list[4], list[5], list[6], list[17],
                     list[14], list[8], list[10], list[11], list[12], list[19], list[15], list[9],
                     list[16], list[23], list[18], list[21], list[20], list[3], list[22], list[1]]
    return new_positions
def L_turn(list):
    new_positions = [list[6], list[1], list[12], list[3], list[10], list[4], list[16], list[7],
                     list[8], list[9], list[11], list[5], list[18], list[13], list[14], list[15],
                     list[22], list[17], list[20], list[19], list[2], list[21], list[0], list[23]]
    return new_positions
def D_turn(list):
    new_positions = [list[9], list[15], list[2], list[3], list[1], list[5], list[6], list[7],
                     list[8], list[19], list[0], list[11], list[12], list[13], list[14], list[18],
                     list[16], list[17], list[4], list[10], list[21], list[23], list[20], list[22]]
    return new_positions
def B_turn(list):
    new_positions = [list[2], list[0], list[3], list[1], list[6], list[7], list[8], list[9],
                     list[21], list[20], list[10], list[11], list[12], list[13], list[14], list[15],
                     list[16], list[17], list[18], list[19], list[5], list[4], list[22], list[23]]
    return new_positions

#Definitions of inverted turns
def Ui_turn(list):
    return U_turn(U_turn(U_turn(list)))
def Fi_turn(list):
    return F_turn(F_turn(F_turn(list)))
def Ri_turn(list):
    return R_turn(R_turn(R_turn(list)))
def Li_turn(list):
    return L_turn(L_turn(L_turn(list)))
def Di_turn(list):
    return D_turn(D_turn(D_turn(list)))
def Bi_turn(list):
    return B_turn(B_turn(B_turn(list)))

normal_moves = [U_turn, F_turn, R_turn, L_turn, D_turn, B_turn]
inverted_moves = [Ui_turn, Fi_turn, Ri_turn, Li_turn, Di_turn, Bi_turn]
list_of_possible_moves = normal_moves + inverted_moves
list_of_probabilities = [1, 6, 27, 120, 534, 2256, 8969, 33058, 114149, 360508, 930588, 1350852, 782536, 90280, 276]



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


#Definitions for solving method
def solve_with_number(scramble, number_of_turns, attemps, count=0):
    scrambled_positions = do_alg_silent(original_positions0, scramble)

    for attemp in range(attemps):
        random_move_list = [random.choice(list_of_possible_moves) for i in range(number_of_turns)]
        if scrambled_positions in [do_alg_silent(original_positions0, random_move_list),
                                   do_alg_silent(original_positions1, random_move_list),
                                   do_alg_silent(original_positions2, random_move_list),
                                   do_alg_silent(original_positions3, random_move_list),
                                   do_alg_silent(original_positions4, random_move_list),
                                   do_alg_silent(original_positions5, random_move_list),
                                   do_alg_silent(original_positions6, random_move_list),
                                   do_alg_silent(original_positions7, random_move_list),
                                   do_alg_silent(original_positions8, random_move_list),
                                   do_alg_silent(original_positions9, random_move_list)]:

            print(f"I found a \033[1;35m{len(correct_alg([move.__name__ for move in reverse_alg(random_move_list)]))}"
                  f" move solution\033[0m:", correct_alg([move.__name__ for move in reverse_alg(random_move_list)]))
            print("The scramble was:", [move.__name__ for move in scramble])
            print(f"I needed {attemp+1} additional attemps")
            return True

def try_to_solve(scramble, count=0):
    total_attempts = 0
    for i in range(15):                                                            #gods number is 14 + solved position
        total_attempts += list_of_probabilities[i]
        print(f"I calculated \033[1;35m{i}\033[0m moves max attempts: \033[1;35m{total_attempts} \033[0m")
        if solve_with_number(scramble, i, list_of_probabilities[i]) == True:       #It doesn't try to find the
            return True                                                   #perfect solution

def solve_until_solution_found(scramble):              #Does try_to_solve until a solution is found.
    while try_to_solve(scramble) != True:
        try_to_solve(scramble)




hardest_scramble = [F_turn, F_turn, U_turn, F_turn, F_turn, U_turn, U_turn,
                    R_turn, R_turn, U_turn, R_turn, R_turn, U_turn]

easy_scramble = [Ri_turn, Ui_turn, Ri_turn, L_turn, Di_turn, R_turn, R_turn, Di_turn, Li_turn]

random_scramble = [random.choice(list_of_possible_moves) for i in range(6)]

solve_until_solution_found(random_scramble)
