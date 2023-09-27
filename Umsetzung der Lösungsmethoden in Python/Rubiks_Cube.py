import random


class Rubiks_Cube:
    def __init__(self, cp, cr = ["Y", "B", "R", "G", "O", "W"], M_rotations = 0, rotationlist = []):
        self.cp = cp
        self.cr = cr
        self.rotationlist = rotationlist
        self.M_rotations = M_rotations

    def update_rotationlist(self):
        i = 0
        while i < len(self.rotationlist) - 3:
            if self.rotationlist[i] == self.rotationlist[i + 1] == self.rotationlist[i + 2] == self.rotationlist[i + 3]:
                del self.rotationlist[i:i + 4]
            else:
                i += 1

    def is_position_solved(self, pos):
        if self.cp[pos] == pos:
            return True
        else:
            return False

    def reset(self):
        self.cp = op[0:48]
        self.rotationlist = []
        self.M_rotations = 0
        return self

    def Fturn(self):
        self.cp = [self.cp[0], self.cp[1], self.cp[5], self.cp[6], self.cp[4], self.cp[20], self.cp[21], self.cp[7],
                   self.cp[11], self.cp[8], self.cp[9], self.cp[10], self.cp[3], self.cp[13], self.cp[2], self.cp[15],
                   self.cp[16], self.cp[17], self.cp[18], self.cp[19], self.cp[14], self.cp[12], self.cp[22], self.cp[23],
                   self.cp[24], self.cp[25], self.cp[29], self.cp[27], self.cp[28], self.cp[44], self.cp[30], self.cp[31],
                   self.cp[35], self.cp[32], self.cp[33], self.cp[34], self.cp[36], self.cp[37], self.cp[38], self.cp[26],
                   self.cp[40], self.cp[41], self.cp[42], self.cp[43], self.cp[39], self.cp[45], self.cp[46], self.cp[47]]
    def Fiturn(self):
        self.cp = [self.cp[0], self.cp[1], self.cp[14], self.cp[12], self.cp[4], self.cp[2], self.cp[3], self.cp[7],
                   self.cp[9], self.cp[10], self.cp[11], self.cp[8], self.cp[21], self.cp[13], self.cp[20], self.cp[15],
                   self.cp[16], self.cp[17], self.cp[18], self.cp[19], self.cp[5], self.cp[6], self.cp[22], self.cp[23],
                   self.cp[24], self.cp[25], self.cp[39], self.cp[27], self.cp[28], self.cp[26], self.cp[30], self.cp[31],
                   self.cp[33], self.cp[34], self.cp[35], self.cp[32], self.cp[36], self.cp[37], self.cp[38], self.cp[44],
                   self.cp[40], self.cp[41], self.cp[42], self.cp[43], self.cp[29], self.cp[45], self.cp[46], self.cp[47]]
    def Uturn(self):
        self.cp = [self.cp[3], self.cp[0], self.cp[1], self.cp[2], self.cp[8], self.cp[9], self.cp[6], self.cp[7],
                   self.cp[12], self.cp[13], self.cp[10], self.cp[11], self.cp[16], self.cp[17], self.cp[14], self.cp[15],
                   self.cp[4], self.cp[5], self.cp[18], self.cp[19], self.cp[20], self.cp[21], self.cp[22], self.cp[23],
                   self.cp[27], self.cp[24], self.cp[25], self.cp[26], self.cp[32], self.cp[29], self.cp[30], self.cp[31],
                   self.cp[36], self.cp[33], self.cp[34], self.cp[35], self.cp[40], self.cp[37], self.cp[38], self.cp[39],
                   self.cp[28], self.cp[41], self.cp[42], self.cp[43], self.cp[44], self.cp[45], self.cp[46], self.cp[47]]
    def Uiturn(self):
        self.cp = [self.cp[1], self.cp[2], self.cp[3], self.cp[0], self.cp[16], self.cp[17], self.cp[6], self.cp[7],
                   self.cp[4], self.cp[5], self.cp[10], self.cp[11], self.cp[8], self.cp[9], self.cp[14], self.cp[15],
                   self.cp[12], self.cp[13], self.cp[18], self.cp[19], self.cp[20], self.cp[21], self.cp[22], self.cp[23],
                   self.cp[25], self.cp[26], self.cp[27], self.cp[24], self.cp[40], self.cp[29], self.cp[30], self.cp[31],
                   self.cp[28], self.cp[33], self.cp[34], self.cp[35], self.cp[32], self.cp[37], self.cp[38], self.cp[39],
                   self.cp[36], self.cp[41], self.cp[42], self.cp[43], self.cp[44], self.cp[45], self.cp[46], self.cp[47]]
    def Riturn(self):
        self.cp = [self.cp[0], self.cp[18], self.cp[16], self.cp[3], self.cp[4], self.cp[5], self.cp[6], self.cp[7],
                   self.cp[8], self.cp[1], self.cp[2], self.cp[11], self.cp[13], self.cp[15], self.cp[12], self.cp[14],
                   self.cp[23], self.cp[17], self.cp[21], self.cp[19], self.cp[20], self.cp[9], self.cp[22], self.cp[10],
                   self.cp[24], self.cp[43], self.cp[26], self.cp[27], self.cp[28], self.cp[29], self.cp[30], self.cp[31],
                   self.cp[32], self.cp[25], self.cp[34], self.cp[35], self.cp[37], self.cp[38], self.cp[39], self.cp[36],
                   self.cp[40], self.cp[41], self.cp[42], self.cp[45], self.cp[44], self.cp[33], self.cp[46], self.cp[47]]
    def Rturn(self):
        self.cp = [self.cp[0], self.cp[9], self.cp[10], self.cp[3], self.cp[4], self.cp[5], self.cp[6], self.cp[7],
                   self.cp[8], self.cp[21], self.cp[23], self.cp[11], self.cp[14], self.cp[12], self.cp[15], self.cp[13],
                   self.cp[2], self.cp[17], self.cp[1], self.cp[19], self.cp[20], self.cp[18], self.cp[22], self.cp[16],
                   self.cp[24], self.cp[33], self.cp[26], self.cp[27], self.cp[28], self.cp[29], self.cp[30], self.cp[31],
                   self.cp[32], self.cp[45], self.cp[34], self.cp[35], self.cp[39], self.cp[36], self.cp[37], self.cp[38],
                   self.cp[40], self.cp[41], self.cp[42], self.cp[25], self.cp[44], self.cp[43], self.cp[46], self.cp[47]]
    def Liturn(self):
        self.cp = [self.cp[8], self.cp[1], self.cp[2], self.cp[11], self.cp[5], self.cp[6], self.cp[7], self.cp[4],
                   self.cp[20], self.cp[9], self.cp[10], self.cp[22], self.cp[12], self.cp[13], self.cp[14], self.cp[15],
                   self.cp[16], self.cp[3], self.cp[18], self.cp[0], self.cp[19], self.cp[21], self.cp[17], self.cp[23],
                   self.cp[24], self.cp[25], self.cp[26], self.cp[35], self.cp[29], self.cp[30], self.cp[31], self.cp[28],
                   self.cp[32], self.cp[33], self.cp[34], self.cp[47], self.cp[36], self.cp[37], self.cp[38], self.cp[39],
                   self.cp[40], self.cp[27], self.cp[42], self.cp[43], self.cp[44], self.cp[45], self.cp[46], self.cp[41]]
    def Lturn(self):
        self.cp = [self.cp[19], self.cp[1], self.cp[2], self.cp[17], self.cp[7], self.cp[4], self.cp[5], self.cp[6],
                   self.cp[0], self.cp[9], self.cp[10], self.cp[3], self.cp[12], self.cp[13], self.cp[14], self.cp[15],
                   self.cp[16], self.cp[22], self.cp[18], self.cp[20], self.cp[8], self.cp[21], self.cp[11], self.cp[23],
                   self.cp[24], self.cp[25], self.cp[26], self.cp[41], self.cp[31], self.cp[28], self.cp[29], self.cp[30],
                   self.cp[32], self.cp[33], self.cp[34], self.cp[27], self.cp[36], self.cp[37], self.cp[38], self.cp[39],
                   self.cp[40], self.cp[47], self.cp[42], self.cp[43], self.cp[44], self.cp[45], self.cp[46], self.cp[35]]
    def Diturn(self):
        self.cp = [self.cp[0], self.cp[1], self.cp[2], self.cp[3], self.cp[4], self.cp[5], self.cp[10], self.cp[11],
                   self.cp[8], self.cp[9], self.cp[15], self.cp[14], self.cp[12], self.cp[13], self.cp[18], self.cp[19],
                   self.cp[16], self.cp[17], self.cp[7], self.cp[6], self.cp[21], self.cp[23], self.cp[20], self.cp[22],
                   self.cp[24], self.cp[25], self.cp[26], self.cp[27], self.cp[28], self.cp[29], self.cp[34], self.cp[31],
                   self.cp[32], self.cp[33], self.cp[38], self.cp[35], self.cp[36], self.cp[37], self.cp[42], self.cp[39],
                   self.cp[40], self.cp[41], self.cp[30], self.cp[43], self.cp[45], self.cp[46], self.cp[47], self.cp[44]]
    def Dturn(self):
        self.cp = [self.cp[0], self.cp[1], self.cp[2], self.cp[3], self.cp[4], self.cp[5], self.cp[19], self.cp[18],
                   self.cp[8], self.cp[9], self.cp[6], self.cp[7], self.cp[12], self.cp[13], self.cp[11], self.cp[10],
                   self.cp[16], self.cp[17], self.cp[14], self.cp[15], self.cp[22], self.cp[20], self.cp[23], self.cp[21],
                   self.cp[24], self.cp[25], self.cp[26], self.cp[27], self.cp[28], self.cp[29], self.cp[42], self.cp[31],
                   self.cp[32], self.cp[33], self.cp[30], self.cp[35], self.cp[36], self.cp[37], self.cp[34], self.cp[39],
                   self.cp[40], self.cp[41], self.cp[38], self.cp[43], self.cp[47], self.cp[44], self.cp[45], self.cp[46]]
    def Bturn(self):
        self.cp = [self.cp[13], self.cp[15], self.cp[2], self.cp[3], self.cp[1], self.cp[5], self.cp[6], self.cp[0],
                   self.cp[8], self.cp[9], self.cp[10], self.cp[11], self.cp[12], self.cp[23], self.cp[14], self.cp[22],
                   self.cp[18], self.cp[16], self.cp[19], self.cp[17], self.cp[20], self.cp[21], self.cp[4], self.cp[7],
                   self.cp[37], self.cp[25], self.cp[26], self.cp[27], self.cp[28], self.cp[29], self.cp[30], self.cp[24],
                   self.cp[32], self.cp[33], self.cp[34], self.cp[35], self.cp[36], self.cp[46], self.cp[38], self.cp[39],
                   self.cp[43], self.cp[40], self.cp[41], self.cp[42], self.cp[44], self.cp[45], self.cp[31], self.cp[47]]
    def Biturn(self):
        self.cp = [self.cp[7], self.cp[4], self.cp[2], self.cp[3], self.cp[22], self.cp[5], self.cp[6], self.cp[23],
                   self.cp[8], self.cp[9], self.cp[10], self.cp[11], self.cp[12], self.cp[0], self.cp[14], self.cp[1],
                   self.cp[17], self.cp[19], self.cp[16], self.cp[18], self.cp[20], self.cp[21], self.cp[15], self.cp[13],
                   self.cp[31], self.cp[25], self.cp[26], self.cp[27], self.cp[28], self.cp[29], self.cp[30], self.cp[46],
                   self.cp[32], self.cp[33], self.cp[34], self.cp[35], self.cp[36], self.cp[24], self.cp[38], self.cp[39],
                   self.cp[41], self.cp[42], self.cp[43], self.cp[40], self.cp[44], self.cp[45], self.cp[37], self.cp[47]]

    def U2turn(self):
        self.Uturn()
        self.Uturn()
    def F2turn(self):
        self.Fturn()
        self.Fturn()
    def R2turn(self):
        self.Rturn()
        self.Rturn()
    def L2turn(self):
        self.Lturn()
        self.Lturn()
    def B2turn(self):
        self.Bturn()
        self.Bturn()
    def D2turn(self):
        self.Dturn()
        self.Dturn()
    def no_move(self):
        pass
    def yturn(self):
        self.rotationlist += ["Y"]
    def xturn(self):
        self.rotationlist += ["X"]
    def y2turn(self):
        self.yturn()
        self.yturn()
    def yiturn(self):
        self.yturn()
        self.yturn()
        self.yturn()
    def x2turn(self):
        self.xturn()
        self.xturn()
    def xiturn(self):
        self.xturn()
        self.xturn()
        self.xturn()
    def Miturn(self):
        self.cp = [self.cp[0], self.cp[1], self.cp[2], self.cp[3], self.cp[4], self.cp[5], self.cp[6], self.cp[7],
                   self.cp[8], self.cp[9], self.cp[10], self.cp[11], self.cp[12], self.cp[13], self.cp[14], self.cp[15],
                   self.cp[16], self.cp[17], self.cp[18], self.cp[19], self.cp[20], self.cp[21], self.cp[22], self.cp[23],
                   self.cp[32], self.cp[25], self.cp[34], self.cp[27], self.cp[28], self.cp[29], self.cp[30], self.cp[31],
                   self.cp[44], self.cp[33], self.cp[46], self.cp[35], self.cp[36], self.cp[37], self.cp[38], self.cp[39],
                   self.cp[26], self.cp[41], self.cp[24], self.cp[43], self.cp[42], self.cp[45], self.cp[40], self.cp[47]]
        self.M_rotations -= 1

    def Mturn(self):
        self.cp = [self.cp[0], self.cp[1], self.cp[2], self.cp[3], self.cp[4], self.cp[5], self.cp[6], self.cp[7],
                   self.cp[8], self.cp[9], self.cp[10], self.cp[11], self.cp[12], self.cp[13], self.cp[14], self.cp[15],
                   self.cp[16], self.cp[17], self.cp[18], self.cp[19], self.cp[20], self.cp[21], self.cp[22], self.cp[23],
                   self.cp[42], self.cp[25], self.cp[40], self.cp[27], self.cp[28], self.cp[29], self.cp[30], self.cp[31],
                   self.cp[24], self.cp[33], self.cp[26], self.cp[35], self.cp[36], self.cp[37], self.cp[38], self.cp[39],
                   self.cp[46], self.cp[41], self.cp[44], self.cp[43], self.cp[32], self.cp[45], self.cp[34], self.cp[47]]
        self.M_rotations += 1

    def M2turn(self):
        self.Mturn()
        self.Mturn()


    move_dict = {
        "R": lambda self: self.Rturn(),
        "Ri": lambda self: self.Riturn(),
        "F": lambda self: self.Fturn(),
        "Fi": lambda self: self.Fiturn(),
        "U": lambda self: self.Uturn(),
        "Ui": lambda self: self.Uiturn(),
        "L": lambda self: self.Lturn(),
        "Li": lambda self: self.Liturn(),
        "B": lambda self: self.Bturn(),
        "Bi": lambda self: self.Biturn(),
        "D": lambda self: self.Dturn(),
        "Di": lambda self: self.Diturn(),
        "U2": lambda self: self.U2turn(),
        "F2": lambda self: self.F2turn(),
        "R2": lambda self: self.R2turn(),
        "L2": lambda self: self.L2turn(),
        "B2": lambda self: self.B2turn(),
        "D2": lambda self: self.D2turn(),
        "": lambda self: self.no_move(),
        "X": lambda self: self.xturn(),
        "xi": lambda self: self.xiturn(),
        "x2": lambda self: self.x2turn(),
        "Y": lambda self: self.yturn(),
        "yi": lambda self: self.yiturn(),
        "y2": lambda self: self.y2turn(),
        " | ": lambda self: self.no_move(),
        "auf": lambda self: self.no_move(),
        "Mi": lambda self: self.Miturn(),
        "M": lambda self: self.Mturn(),
        "M2": lambda self: self.M2turn()
    }


    def doalg(self, alg):
        for k in range(len(alg)):
            self.move_dict[alg[k]](self)
        return self


    def virtualcube(self):
        pos = self.cp

        def colorprint(number):
            yellow_string_list = []
            for element in yellow_side:
                yellow_string_list.append(str(element))
            blue_string_list = []
            for element in blue_side:
                blue_string_list.append(str(element))
            red_string_list = []
            for element in red_side:
                red_string_list.append(str(element))
            green_string_list = []
            for element in green_side:
                green_string_list.append(str(element))
            orange_string_list = []
            for element in orange_side:
                orange_string_list.append(str(element))
            white_string_list = []
            for element in white_side:
                white_string_list.append(str(element))

            if number == "Y":
                print(f"\033[33m[{number} ]", end=" ")
            elif number == "B":
                print(f"\033[34m[{number} ]", end=" ")
            elif number == "R":
                print(f"\033[31m[{number} ]", end=" ")
            elif number == "G":
                print(f"\033[32m[{number} ]", end=" ")
            elif number == "O":
                print(f"\033[35m[{number} ]", end=" ")
            elif number == "W":
                print(f"\033[37m[{number} ]", end=" ")

            elif str(op[number]) in yellow_string_list:
                if len(str(number)) == 1:
                    print(f"\033[33m[{number} ]", end=" ")
                else:
                    print(f"\033[33m[{number}]", end=" ")
            elif str(op[number]) in blue_string_list:
                if len(str(number)) == 1:
                    print(f"\033[34m[{number} ]", end=" ")
                else:
                    print(f"\033[34m[{number}]", end=" ")
            elif str(op[number]) in red_string_list:
                if len(str(number)) == 1:
                    print(f"\033[31m[{number} ]", end=" ")
                else:
                    print(f"\033[31m[{number}]", end=" ")
            elif str(op[number]) in green_string_list:
                if len(str(number)) == 1:
                    print(f"\033[32m[{number} ]", end=" ")
                else:
                    print(f"\033[32m[{number}]", end=" ")
            elif str(op[number]) in orange_string_list:
                if len(str(number)) == 1:
                    print(f"\033[35m[{number} ]", end=" ")
                else:
                    print(f"\033[35m[{number}]", end=" ")
            elif str(op[number]) in white_string_list:
                if len(str(number)) == 1:
                    print(f"\033[37m[{number} ]", end=" ")
                else:
                    print(f"\033[37m[{number}]", end=" ")

        print("                 ", end="")
        colorprint(pos[0])
        colorprint(pos[24])
        colorprint(pos[1])
        print("\n                 ", end="")
        colorprint(pos[27])
        colorprint(self.cr[0])
        colorprint(pos[25])
        print("\n                 ", end="")
        colorprint(pos[3])
        colorprint(pos[26])
        colorprint(pos[2])
        print()
        print()
        colorprint(pos[4])
        colorprint(pos[28])
        colorprint(pos[5])
        print("  ", end="")
        colorprint(pos[8])
        colorprint(pos[32])
        colorprint(pos[9])
        print("  ", end="")
        colorprint(pos[12])
        colorprint(pos[36])
        colorprint(pos[13])
        print("  ", end="")
        colorprint(pos[16])
        colorprint(pos[40])
        colorprint(pos[17])
        print()
        colorprint(pos[31])
        colorprint(self.cr[1])
        colorprint(pos[29])
        print("  ", end="")
        colorprint(pos[35])
        colorprint(self.cr[2])
        colorprint(pos[33])
        print("  ", end="")
        colorprint(pos[39])
        colorprint(self.cr[3])
        colorprint(pos[37])
        print("  ", end="")
        colorprint(pos[43])
        colorprint(self.cr[4])
        colorprint(pos[41])
        print()
        colorprint(pos[7])
        colorprint(pos[30])
        colorprint(pos[6])
        print("  ", end="")
        colorprint(pos[11])
        colorprint(pos[34])
        colorprint(pos[10])
        print("  ", end="")
        colorprint(pos[14])
        colorprint(pos[38])
        colorprint(pos[15])
        print("  ", end="")
        colorprint(pos[18])
        colorprint(pos[42])
        colorprint(pos[19])
        print("\n\n"f"                 ", end="")
        colorprint(pos[20])
        colorprint(pos[44])
        colorprint(pos[21])
        print("\n                 ", end="")
        colorprint(pos[47])
        colorprint(self.cr[5])
        colorprint(pos[45])
        print("\n                 ", end="")
        colorprint(pos[22])
        colorprint(pos[46])
        colorprint(pos[23])
        print("\n\n")
        return self


class Alg:# Diese Klasse wird nur verwendet, um Algorithmen zu modifizieren
    def __init__(self, alg):
        self.alg = alg

    def mirror(self):
        for i in range(len(self.alg)):
            if self.alg[i] == "U":
                self.alg[i] = "Ui"
            elif self.alg[i] == "Ui":
                self.alg[i] = "U"
            elif self.alg[i] == "D":
                self.alg[i] = "Di"
            elif self.alg[i] == "Di":
                self.alg[i] = "D"
            elif self.alg[i] == "R":
                self.alg[i] = "Li"
            elif self.alg[i] == "Li":
                self.alg[i] = "R"
            elif self.alg[i] == "L":
                self.alg[i] = "Ri"
            elif self.alg[i] == "Ri":
                self.alg[i] = "L"
            elif self.alg[i] == "R2":
                self.alg[i] = "L2"
            elif self.alg[i] == "L2":
                self.alg[i] = "R2"
            elif self.alg[i] == "F":
                self.alg[i] = "Fi"
            elif self.alg[i] == "Fi":
                self.alg[i] = "F"
            elif self.alg[i] == "B":
                self.alg[i] = "Bi"
            elif self.alg[i] == "Bi":
                self.alg[i] = "B"
        return self.alg

    def rotate_left(self):
        for i in range(len(self.alg)):
            if self.alg[i] == "R":
                self.alg[i] = "F"
            elif self.alg[i] == "Ri":
                self.alg[i] = "Fi"
            elif self.alg[i] == "R2":
                self.alg[i] = "F2"

            elif self.alg[i] == "F":
                self.alg[i] = "L"
            elif self.alg[i] == "Fi":
                self.alg[i] = "Li"
            elif self.alg[i] == "F2":
                self.alg[i] = "L2"

            elif self.alg[i] == "L":
                self.alg[i] = "B"
            elif self.alg[i] == "Li":
                self.alg[i] = "Bi"
            elif self.alg[i] == "L2":
                self.alg[i] = "B2"

            elif self.alg[i] == "B":
                self.alg[i] = "R"
            elif self.alg[i] == "Bi":
                self.alg[i] = "Ri"
            elif self.alg[i] == "B2":
                self.alg[i] = "R2"
        return self.alg

    def rotate_right(self):
        for _ in range(3):
            self.rotate_left()
            return self.alg



op = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, "y", "w", "r", "b", "g", "o"]
edges = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", op[24], op[25], op[26], op[27], op[28], op[29], op[30], op[31], op[32], op[33], op[34], op[35], op[36], op[37], op[38], op[39], op[40], op[41], op[42], op[43], op[44], op[45], op[46], op[47]]
corners = [op[0], op[1], op[2], op[3], op[4], op[5], op[6], op[7], op[8], op[9], op[10], op[11], op[12], op[13], op[14], op[15], op[16], op[17], op[18], op[19], op[20], op[21], op[22], op[23], "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

red_side = {op[8], op[9], op[10], op[11], op[32], op[33], op[34], op[35]}
yellow_side = {op[0], op[1], op[2], op[3], op[24], op[25], op[26], op[27]}
white_side = {op[20], op[21], op[22], op[23], op[44], op[45], op[46], op[47]}
green_side = {op[12], op[13], op[14], op[15], op[36], op[37], op[38], op[39]}
orange_side = {op[16], op[17], op[18], op[19], op[40], op[41], op[42], op[43]}
blue_side = {op[4], op[5], op[6], op[7], op[28], op[29], op[30], op[31]}
sides = [red_side, yellow_side, white_side, green_side, orange_side, blue_side]
red_layer = {op[2], op[26], op[3], op[12], op[14], op[39], op[20], op[21], op[44], op[5], op[6], op[29]} | red_side
yellow_layer = {op[4], op[5], op[28], op[8], op[9], op[32], op[12], op[13], op[36], op[16], op[17], op[40]} | yellow_side
white_layer = {op[6], op[7], op[30], op[11], op[10], op[34], op[14], op[38], op[15], op[18], op[19], op[42]} | white_side
green_layer = {op[9], op[10], op[33], op[2], op[1], op[25], op[16], op[18], op[43], op[21], op[23], op[45]} | green_side
orange_layer = {op[0], op[1], op[24], op[4], op[7], op[31], op[22], op[23], op[46], op[13], op[15], op[37]} | orange_side
blue_layer = {op[17], op[19], op[41], op[0], op[3], op[27], op[8], op[11], op[35], op[20], op[22], op[47]} | blue_side
layers = [yellow_layer, white_layer, green_layer, orange_layer, blue_layer]

edges_set = {op[i] for i in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]}
corners_set = {op[i] for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]}
oriented_edges = set(op) & edges_set - blue_side - green_side - ((red_side | orange_side) & (yellow_layer | white_layer))
normal_moves = ["R", "U", "F", "L", "B", "D"]
inverted_moves = ["Ri", "Ui", "Fi", "Li", "Bi", "Di"]
double_moves = ["R2", "U2", "F2", "L2", "B2", "D2"]
possible_moves = normal_moves + inverted_moves
cube1 = Rubiks_Cube(op)

sexymove = ["R", "U", "Ri", "Ui"]
fsexymove = ["F"] + sexymove + ["Fi"]
bottom_sexymove = ["Ri", "Di", "R", "D"]
sune = ["R", "U", "Ri", "U", "R", "U2", "Ri"]
breakdance = ["U", "R", "Ui", "Li", "U", "Ri", "Ui", "L"]
lblalg1 = Alg(["Ri", "Fi", "R", "U", "R", "Ui", "Ri", "F"])
lblalg2 = Alg(list(lblalg1.alg))
lblalg2.rotate_left()
lblalg3 = Alg(list(lblalg1.alg))
lblalg3.rotate_left()
lblalg3.rotate_left()
lblalg3.rotate_left()
lblalg4 = Alg(list(lblalg1.alg))
lblalg4.rotate_left()
lblalg4.rotate_left()
lblalg5 = Alg(list(lblalg1.alg))
lblalg5.mirror()
lblalg6 = Alg(list(lblalg2.alg))
lblalg6.mirror()
lblalg7 = Alg(list(lblalg3.alg))
lblalg7.mirror()
lblalg8 = Alg(list(lblalg4.alg))
lblalg8.mirror()

# 0 edges, less than 2 corners
oll1 = ["R", "U2", "R2", "F", "R", "Fi", "U2", "Ri", "F", "R", "Fi"]
oll2 = ["Ri", "U2", "L", "Fi", "Li", "U2", "L", "F", "Li", "U2", "R"]
oll3 = ["F", "U", "R", "Ui", "Ri", "Fi", "U", "F", "R", "U", "Ri", "Ui", "Fi"]
oll4 = ["F", "U", "R", "Ui", "Ri", "Fi", "Ui", "F", "R", "U", "Ri", "Ui", "Fi"]
oll_group1 = [oll1, oll2, oll3, oll4]

# clock edges, 0 corners
oll47 = ["Fi", "Li", "Ui", "L", "U", "Li", "Ui", "L", "U", "F"]
oll48 = ["F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
oll49 = ["R", "Bi", "R2", "F", "R2", "B", "R2", "Fi", "R"]
oll50 = ["Ri", "F", "R2", "Bi", "R2", "Fi", "R2", "B", "Ri"]
oll53 = ["Fi", "L", "F", "Li", "U2", "F2", "Ri", "Fi", "R", "Fi"]
oll54 = ["F", "Ri", "Fi", "R", "U2", "F2", "L", "F", "Li", "F"]
oll_group2 = [oll47, oll48, oll49, oll50, oll53, oll54]


# clock edges, 1 corner
oll5 = ["Li", "Ui", "L2", "Fi", "Li", "F2", "Ui", "Fi"]
oll6 = ["R", "U", "R2", "F", "R", "F2", "U", "F"]
oll7 = ["F", "Ri", "Fi", "R", "U2", "R", "U2", "Ri"]
oll8 = ["R", "U2", "Ri", "U2", "Ri", "F", "R", "Fi"]
oll9 = ["R", "U", "Ri", "Ui", "Ri", "F", "R2", "U", "Ri", "Ui", "Fi"]
oll10 = ["R", "U", "Ri", "U", "Ri", "F", "R", "Fi", "R", "U2", "Ri"]
oll11 = ["Fi", "Li", "Ui", "L", "U", "F", "U", "F", "R", "U", "Ri", "Ui", "Fi"]
oll12 = ["F", "R", "U", "Ri", "Ui", "Fi", "U", "F", "R", "U", "Ri", "Ui", "Fi"]
oll_group3 = [oll5, oll6, oll7, oll8, oll9, oll10, oll11, oll12]

#clock edges, 2 corners
oll29 = ["Ri", "F", "R", "Fi", "R", "U2", "Ri", "Ui", "Fi", "Ui", "F"]
oll30 = ["F", "U", "R", "U2", "Ri", "Ui", "R", "U2", "Ri", "Ui", "Fi"]
oll31 = ["Ri", "Ui", "F", "U", "R", "Ui", "Ri", "Fi", "R"]
oll32 = ["L", "U", "Fi", "Ui", "Li", "U", "L", "F", "Li"]
oll35 = ["R", "U2", "R2", "F", "R", "Fi", "R", "U2", "Ri"]
oll36 = ["R", "U", "Ri", "Ui", "Fi", "U2", "F", "U", "R", "U", "Ri"]
oll37 = ["F", "Ri", "Fi", "R", "U", "R", "Ui", "Ri"]
oll38 = ["R", "U", "Ri", "U", "R", "Ui", "Ri", "Ui", "Ri", "F", "R", "Fi"]
oll41 = ["R", "U", "Ri", "U", "R", "U2", "Ri", "F", "R", "U", "Ri", "Ui", "Fi"]
oll42 = ["Ri", "Ui", "R", "Ui", "Ri", "U2", "R", "F", "R", "U", "Ri", "Ui", "Fi"]
oll43 = ["Ri", "Ui", "Fi", "U", "F", "R"]
oll44 = ["F", "U", "R", "Ui", "Ri", "Fi"]
oll_group4 = [oll29, oll30, oll31, oll32, oll35, oll36, oll37, oll38, oll41, oll42, oll43, oll44]

# minus, 0 corners
oll51 = ["F", "U", "R", "Ui", "Ri", "U", "R", "Ui", "Ri", "Fi"]
oll52 = ["Ri", "Ui", "R", "Ui", "Ri", "U", "Fi", "U", "F", "R"]
oll55 = ["R", "U2", "R2", "Ui", "R", "Ui", "Ri", "U2", "F", "R", "Fi"]
oll56 = ["F", "R", "U", "Ri", "Ui", "R", "Fi", "L", "F", "Ri", "Fi", "Li"]
oll_group5 = [oll51, oll52, oll55, oll56]

# minus edges, 1 corner
oll13 = ["F", "U", "R", "U2", "Ri", "Ui", "R", "U", "Ri", "Fi"]
oll14 = ["Ri", "F", "R", "U", "Ri", "Fi", "R", "F", "Ui", "Fi"]
oll15 = ["Ri", "Fi", "R", "Li", "Ui", "L", "U", "Ri", "F", "R"]
oll16 = ["Ri", "F", "R", "U", "Ri", "Ui", "Fi", "R", "Ui", "Ri", "U2", "R"]
oll_group6 = [oll13, oll14, oll15, oll16]

# minus edges, 2 corners
oll33 = ["R", "U", "Ri", "Ui", "Ri", "F", "R", "Fi"]
oll34 = ["R", "U", "R2", "Ui", "Ri", "F", "R", "U", "R", "Ui", "Fi"]
oll39 = ["L", "Fi", "Li", "Ui", "L", "U", "F", "Ui", "Li"]
oll40 = ["Ri", "F", "R", "U", "Ri", "Ui", "Fi", "U", "R"]
oll45 = ["F", "R", "U", "Ri", "Ui", "Fi"]
oll46 = ["Ri", "Ui", "Ri", "F", "R", "Fi", "U", "R"]
oll_group7 = [oll33, oll34, oll39, oll40, oll45, oll46]

# dot cases
oll17 = ["R", "U", "Ri", "U", "Ri", "F", "R", "Fi", "U2", "Ri", "F", "R", "Fi"]
oll18 = ["F", "Ri", "Fi", "R", "U2", "F", "Ri", "Fi", "R", "Ui", "R", "Ui", "Ri"]
oll19 = ["Ri", "U2", "F", "R", "U", "Ri", "Ui", "F2", "U2", "F", "R"]
oll20 = ["F", "U", "R", "Ui", "Ri", "Fi", "U2", "Ri", "Ui", "Ri", "F", "R", "Fi", "U", "R"]
oll_group8 = [oll17, oll18, oll19, oll20]

# 4 edges, less than 2 corners
oll21 = ["R", "U2", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "Ui", "Ri"]
oll22 = ["R", "U2", "R2", "Ui", "R2", "Ui", "R2", "U2", "R"]
oll26 = ["Ri", "Ui", "R", "Ui", "Ri", "U2", "R"]
oll27 = ["R", "U", "Ri", "U", "R", "U2", "Ri"]
oll_group9 = [oll21, oll22, oll26, oll27]

# 4 edges, 2 corners
oll23 = ["R2", "D", "Ri", "U2", "R", "Di", "Ri", "U2", "Ri"]
oll24 = ["L", "F", "Ri", "Fi", "Li", "F", "R", "Fi"]
oll25 = ["Ri", "Fi", "Li", "F", "R", "Fi", "L", "F"]
oll_group10 = [oll23, oll24, oll25]

# 2 edges, 4 corners
oll57 = ["Li", "R", "U", "Ri", "Ui", "L", "Ri", "F", "R", "Fi"]
oll28 = ["F", "R", "U", "Ri", "Ui", "F2", "Li", "Ui", "L", "U", "F"]
oll_group11 = [oll57, oll28]

pllAa = ["Ri", "F", "Ri", "B2", "R", "Fi", "Ri", "B2", "R2"]
pllAb = ["R2", "B2", "R", "F", "Ri", "B2", "R", "Fi", "R"]
pllE = ["Ri", "Ui", "Ri", "Di", "R", "Ui", "Ri", "D", "R", "U", "Ri", "Di", "R", "U", "Ri", "D", "R2"]
pllF = ["Ri", "U", "R", "Ui", "R2", "Fi", "Ui", "F", "U", "R", "F", "Ri", "Fi", "R2"]
pllGa = ["R2", "U", "Ri", "U", "Ri", "Ui", "R", "Ui", "R2", "D", "Ui", "Ri", "U", "R", "Di"]
pllGb = ["Ri", "Ui", "R", "U", "Di", "R2", "U", "Ri", "U", "R", "Ui", "R", "Ui", "R2", "D"]
pllGc = ["R2", "Ui", "R", "Ui", "R", "U", "Ri", "U", "R2", "Di", "U", "R", "Ui", "Ri", "D"]
pllGd = ["R", "U", "Ri", "Ui", "D", "R2", "Ui", "R", "Ui", "Ri", "U", "Ri", "U", "R2", "Di"]
pllH = ["R2", "U2", "R", "U2", "R2", "U2", "R2", "U2", "R", "U2", "R2"]
pllJa = ["Li", "Ui", "L", "F", "Li", "Ui", "L", "U", "L", "Fi", "L2", "U", "L"]
pllJb = ["R", "U", "Ri", "Fi", "R", "U", "Ri", "Ui", "Ri", "F", "R2", "Ui", "Ri"]
pllNa = ["L", "Ui", "R", "U2", "Li", "U", "Ri", "L", "Ui", "R", "U2", "Li", "U", "Ri"]
pllNb = ["Ri", "U", "Li", "U2", "R", "Ui", "L", "Ri", "U", "Li", "U2", "R", "Ui", "L"]
pllRa = ["R", "U", "Ri", "Fi", "R", "U2", "Ri", "U2", "Ri", "F", "R", "U", "R", "U2", "Ri"]
pllRb = ["Ri", "U2", "R", "U2", "Ri", "F", "R", "U", "Ri", "Ui", "Ri", "Fi", "R2"]
pllT = ["R", "U", "Ri", "Ui", "Ri", "F", "R2", "Ui", "Ri", "Ui", "R", "U", "Ri", "Fi"]
pllUa = ["R", "Ui", "R", "U", "R", "U", "R", "Ui", "Ri", "Ui", "R2"]
pllUb = ["R2", "U", "R", "U", "Ri", "Ui", "Ri", "Ui", "Ri", "U", "Ri"]
pllV = ["Ri", "U", "Ri", "Ui", "R", "Di", "Ri", "D", "Ri", "U", "Di", "R2", "Ui", "R2", "D", "R2"]
pllY = ["F", "R", "Ui", "Ri", "Ui", "R", "U", "Ri", "Fi", "R", "U", "Ri", "Ui", "Ri", "F", "R", "Fi"]
pllZ = ["Ri", "Ui", "R", "Ui", "R", "U", "R", "Ui", "Ri", "U", "R", "U", "R2", "Ui", "Ri"]
pll_group = [pllAa, pllAb, pllE, pllF, pllGa, pllGb, pllGc, pllGd, pllH, pllJa, pllJb,
             pllNa, pllNb, pllRa, pllRb, pllT, pllUa, pllUb, pllV, pllY, pllZ]


cmll1 = ["U", "R", "U2", "Ri", "Ui", "R", "Ui", "Ri"]
cmll2 = ["U", "Ri", "Ui", "R", "Ui", "Ri", "U", "Ri", "Di", "R", "U", "Ri", "D", "R2"]
cmll3 = ["U", "F", "R", "Ui", "Ri", "U", "R", "U2", "Ri", "Ui", "Fi"]
cmll4 = ["U2", "R", "U2", "Ri", "U2", "Ri", "F", "R", "Fi"]
cmll5 = ["Ri", "U", "L", "Ui", "R", "U", "Li"]
cmll6 = ["R", "U2", "Ri", "F", "Ri", "Fi", "R", "Ui", "R", "Ui", "Ri"]
cmll7 = ["R", "U2", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "Ui", "Ri"]
cmll8 = ["Ui", "R", "U", "Ri", "U", "R", "U", "Li", "U", "Ri", "Ui", "L"]
cmll9 = ["U", "R", "U2", "R2", "F", "R", "Fi", "U2", "Ri", "F", "R", "Fi"]
cmll10 = ["F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
cmll11 = ["Fi", "R", "D2", "Ri", "F", "U2", "Fi", "R", "D2", "Ri", "F"]
cmll12 = ["Ri", "U2", "Ri", "Di", "R", "U2", "Ri", "D", "R2"]
cmll13 = ["U", "R", "U2", "R", "D", "Ri", "U2", "R", "Di", "R2"]
cmll14 = ["U", "F", "Ri", "Fi", "R", "U", "R", "Ui", "Ri"]
cmll15 = ["U", "F", "R", "Ui", "Ri", "Ui", "R", "U", "Ri", "Fi"]
cmll16 = ["U", "R", "U2", "R2", "F", "R", "Fi", "R", "U2", "Ri"]
cmll17 = ["Ri", "U", "Li", "U2", "R", "Ui", "Ri", "U2", "R", "L"]
cmll18 = ["F", "R", "Ui", "Ri", "Ui", "R", "U", "Ri", "Fi", "R", "U", "Ri", "Ui", "Ri", "F", "R", "Fi"]
cmll19 = ["F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
cmll20 = ["U", "F", "Ri", "Fi", "R", "U2", "R", "Ui", "Ri", "U", "R", "U2", "Ri"]
cmll21 = ["Ui", "Ri", "F", "R", "U", "F", "Ui", "R", "U", "Ri", "Ui", "Fi"]
cmll22 = ["R", "U2", "Ri", "Ui", "R", "U", "Ri", "U2", "Ri", "F", "R", "Fi"]
cmll23 = ["R", "Ui", "Li", "U", "Ri", "U", "L", "U", "Li", "U", "L"]
cmll24 = ["Li", "Ui", "L", "Ui", "Li", "U", "L", "F", "R", "U", "Ri", "Fi"]
cmll25 = ["R", "U", "Ri", "U", "R", "U2", "Ri"]
cmll26 = ["Li", "U2", "L", "U2", "L", "Fi", "Li", "F"]
cmll27 = ["F", "Ri", "Fi", "R", "U2", "R", "U2", "Ri"]
cmll28 = ["Ui", "R", "U", "Ri", "U", "R", "Ui", "R", "D", "Ri", "Ui", "R", "Di", "R2"]
cmll29 = ["R", "Ui", "Li", "U", "Ri", "Ui", "L"]
cmll30 = ["U2", "R", "U", "Ri", "U", "Ri", "F", "R", "Fi", "R", "U2", "Ri"]
cmll31 = ["R", "U2", "Ri", "Ui", "R", "Ui", "R2", "U2", "R", "U", "Ri", "U", "R"]
cmll32 = ["Li", "B", "L", "U2", "R2", "F", "R", "Fi", "R"]
cmll33 = ["U", "Li", "Ui", "L", "U", "L", "Fi", "Li", "F"]
cmll34 = ["F", "Ri", "Ui", "R", "Fi", "Ri", "U", "Fi", "R"]
cmll35 = ["Ui", "R", "U", "Ri", "Ui", "Ri", "F", "R", "Fi"]
cmll36 = ["R2", "Ui", "R", "F", "Ri", "U", "R2", "Ui", "Ri", "Fi", "R"]
cmll37 = ["Ri", "Ui", "R", "Ui", "Ri", "U2", "R2", "U", "Ri", "U", "R", "U2", "Ri"]
cmll38 = ["Ui", "F", "R2", "D", "Ri", "U", "R", "Di", "R2", "Ui", "Fi"]
cmll39 = ["U2", "R2", "D", "Ri", "U2", "R", "Di", "Ri", "U2", "Ri"]
cmll40 = ["U2", "Ri", "F", "Ui", "R", "F", "Ri", "U", "R", "Fi"]
cmll41 = ["R2", "Di", "R", "U2", "Ri", "D", "R", "U2", "R"]
cmll42 = ["Ui", "F", "R", "U", "Ri", "Ui", "Fi"]

cmll_group1 = [cmll1, cmll2, cmll3, cmll4, cmll5, cmll6, cmll25, cmll26, cmll27, cmll28, cmll29, cmll30]
cmll_group2 = [cmll7, cmll8, cmll9, cmll10, cmll19, cmll20, cmll21, cmll22, cmll23, cmll24, cmll17, cmll18]
cmll_group3 = [cmll11, cmll12, cmll13, cmll14, cmll15, cmll16, cmll31, cmll32, cmll33, cmll34, cmll35,
               cmll36, cmll37, cmll38, cmll39, cmll40, cmll41, cmll42]

l6e1 = ["R", "Ui", "Ri", "M", "Ui", "Mi", "U", "R", "Mi", "U", "Ri", "M"]
l6e2 = ["Mi", "U2", "Mi", "U2", "M", "Ui", "Mi"]
l6e3 = ["Mi", "U", "Mi", "Ui", "M", "Ui", "M"]
l6e4 = ["Mi", "Ui", "Mi"]
l6e5 = ["M", "Ui", "Mi"]
l6e6 = ["Mi", "U2", "Mi", "U2", "Mi", "Ui", "Mi"]
l6e7 = ["Mi", "U", "M", "Ui", "Mi", "Ui", "Mi"]
l6e8 = ["Mi", "U", "Mi", "U2", "Mi", "Ui", "Mi"]
l6e9 = ["Mi", "Ui", "Mi", "Ui", "M", "Ui", "Mi"]
l6e10 = ["Mi", "Ui", "M", "Ui", "Mi", "Ui", "Mi"]
l6e11 = ["M2", "Ui", "Mi", "Ui", "Mi"]
l6e_group = [l6e1, l6e2, l6e3, l6e4, l6e5, l6e6, l6e7, l6e8, l6e9, l6e10, l6e11]

ell1 = ["L", "U", "L", "Fi", "Li", "F", "Ui", "Li", "Ri", "Ui", "Ri", "F", "R", "Fi", "U", "R"]
ell2 = ["Mi", "U", "Mi", "U", "Mi", "U2", "M", "U", "M", "U", "M"]
ell3 = ["Mi", "U2", "M", "U2", "Mi", "Ui", "M", "U2", "Mi", "U2", "M"]
ell4 = ["M", "U", "R", "U", "Ri", "Ui", "M2", "U", "R", "Ui", "Ri", "M"]
ell5 = ["Mi", "U", "M", "U", "Mi", "U2", "Mi", "U", "Mi", "U", "M", "U", "Mi", "U", "Mi"]
ell6 = ["Mi", "Ui", "M", "U", "Mi", "U", "M", "U", "Mi", "U", "M", "U2", "Mi", "Ui", "M"]
ell7 = ["M", "Ui", "Mi", "U2", "M", "Ui", "M2", "U", "M", "U2", "Mi", "U", "M"]
ell8 = ["Mi", "Ui", "Mi", "U2", "Mi", "U", "M", "Ui", "Mi", "U2", "M", "U", "M2"]
ell9 = ["Mi", "U", "Mi", "U2", "Mi", "Ui", "M", "U", "Mi", "U2", "M", "Ui", "M2"]
ell10 = ["M2", "U", "M", "Ui", "Mi", "Ui", "Mi", "U", "Mi", "U", "Mi", "Ui", "M"]
ell11 = ["Mi", "U", "Mi", "U2", "M", "U", "M2", "U", "Mi"]
ell12 = ["Mi", "Ui", "Mi", "U2", "M", "Ui", "M2", "Ui", "Mi"]
ell13 = ["M2", "Ui", "Mi", "U2", "M", "U", "Mi", "Ui", "M", "U2", "M", "U", "M"]
ell14 = ["R2", "F", "R", "U", "R", "Ui", "R2", "Fi", "R", "U", "R", "U", "Ri", "U2", "R"]
ell15 = ["Mi", "U", "M", "Ui", "Mi", "U", "M", "U", "Mi", "U2", "M"]
ell16 = ["Ri", "Ui", "Ri", "F", "R", "Fi", "U", "R", "F", "R", "U", "Ri", "Ui", "Fi"]
ell17 = ["F", "R", "U", "Ri", "Ui", "Fi", "Ri", "Ui", "Ri", "F", "R", "Fi", "U", "R"]
ell18 = ["", "R", "U", "Ri", "Ui", "Mi", "U", "R", "Ui", "Ri", "M"]
ell19 = ["M", "Ui", "Mi", "U2", "M", "Ui", "Mi"]
ell20 = ["F", "R", "U", "Ri", "Ui", "F2", "Li", "Ui", "L", "U", "F"]
ell21 = ["Mi", "Ui", "M", "U", "Mi", "Ui", "M", "Ui", "Mi", "U2", "M"]
ell22 = ["M", "U", "Mi", "U2", "M", "U", "Mi"]
ell23 = ["Ri", "Ui", "R", "U", "M", "Ui", "Ri", "U", "R", "Mi"]
ell24 = ["Ri", "M", "Ui", "R", "U", "Mi", "Ui", "Ri", "U", "R"]
ell25 = ["R", "Mi", "U", "Ri", "Ui", "M", "U", "R", "Ui", "Ri"]
ell_group = [ell1, ell2, ell3, ell4, ell5, ell6, ell7, ell8, ell9, ell10, ell11, ell12, ell13, ell14,
             ell15, ell16, ell17, ell18, ell19, ell20, ell21, ell22, ell23, ell24, ell25, pllUa, pllUb, pllZ, pllH, ["auf"]]

cll1 = ["U", "R", "U2", "Ri", "Ui", "R", "Ui", "Ri"]
cll2 = ["U", "Ri", "Ui", "R", "Ui", "Ri", "U", "Ri", "Di", "R", "U", "Ri", "D", "R2"]
cll3 = ["U", "F", "R", "Ui", "Ri", "U", "R", "U2", "Ri", "Ui", "Fi"]
cll4 = ["U2", "R", "U2", "Ri", "U2", "Ri", "F", "R", "Fi"]
cll5 = ["Ri", "U", "L", "Ui", "R", "U", "Li"]
cll6 = ["R", "U2", "Ri", "F", "Ri", "Fi", "R", "Ui", "R", "Ui", "Ri"]
cll7 = ["R", "U2", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "Ui", "Ri"]
cll8 = ["Ui", "R", "U", "Ri", "U", "R", "U", "Li", "U", "Ri", "Ui", "L"]
cll9 = ["U", "R", "U2", "R2", "F", "R", "Fi", "U2", "Ri", "F", "R", "Fi"]
cll10 = ["F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
cll11 = ["Fi", "R", "D2", "Ri", "F", "U2", "Fi", "R", "D2", "Ri", "F"]
cll12 = ["Ri", "U2", "Ri", "Di", "R", "U2", "Ri", "D", "R2"]
cll13 = ["U", "R", "U2", "R", "D", "Ri", "U2", "R", "Di", "R2"]
cll14 = ["U", "F", "Ri", "Fi", "R", "U", "R", "Ui", "Ri"]
cll15 = ["U", "F", "R", "Ui", "Ri", "Ui", "R", "U", "Ri", "Fi"]
cll16 = ["U", "R", "U2", "R2", "F", "R", "Fi", "R", "U2", "Ri"]
cll17 = ["Ri", "U", "Li", "U2", "R", "Ui", "Ri", "U2", "R", "L"]
cll18 = ["F", "R", "Ui", "Ri", "Ui", "R", "U", "Ri", "Fi", "R", "U", "Ri", "Ui", "Ri", "F", "R", "Fi"]
cll19 = ["F", "R", "U", "Ri", "Ui", "R", "U", "Ri", "Ui", "Fi"]
cll20 = ["U", "F", "Ri", "Fi", "R", "U2", "R", "Ui", "Ri", "U", "R", "U2", "Ri"]
cll21 = ["F", "Ri", "Fi", "U2", "R", "U", "Ri", "U", "R2", "U2", "Ri"]
cll22 = ["R", "U2", "Ri", "Ui", "R", "U", "Ri", "U2", "Ri", "F", "R", "Fi"]
cll23 = ["R", "Ui", "Li", "U", "Ri", "U", "L", "U", "Li", "U", "L"]
cll24 = ["Li", "Ui", "L", "Ui", "Li", "U", "L", "F", "R", "U", "Ri", "Fi"]
cll25 = ["R", "U", "Ri", "U", "R", "U2", "Ri"]
cll26 = ["Li", "U2", "L", "U2", "L", "Fi", "Li", "F"]
cll27 = ["F", "Ri", "Fi", "R", "U2", "R", "U2", "Ri"]
cll28 = ["Ui", "R", "U", "Ri", "U", "R", "Ui", "R", "D", "Ri", "Ui", "R", "Di", "R2"]
cll29 = ["R", "Ui", "Li", "U", "Ri", "Ui", "L"]
cll30 = ["U2", "R", "U", "Ri", "U", "Ri", "F", "R", "Fi", "R", "U2", "Ri"]
cll31 = ["R", "U2", "Ri", "Ui", "R", "Ui", "R2", "U2", "R", "U", "Ri", "U", "R"]
cll32 = ["Ri", "U", "R", "U2", "Li", "Ri", "U", "R", "Ui", "L"]
cll33 = ["U", "Li", "Ui", "L", "U", "L", "Fi", "Li", "F"]
cll34 = ["F", "U", "R", "U2", "Ri", "Ui", "R", "U2", "Ri", "Ui", "Fi"]
cll35 = ["Ui", "R", "U", "Ri", "Ui", "Ri", "F", "R", "Fi"]
cll36 = ["R2", "Ui", "R", "F", "Ri", "U", "R2", "Ui", "Ri", "Fi", "R"]
cll37 = ["Ri", "Ui", "R", "Ui", "Ri", "U2", "R2", "U", "Ri", "U", "R", "U2", "Ri"]
cll38 = ["Ui", "F", "R2", "D", "Ri", "U", "R", "Di", "R2", "Ui", "Fi"]
cll39 = ["U2", "R2", "D", "Ri", "U2", "R", "Di", "Ri", "U2", "Ri"]
cll40 = ["U2", "F", "R", "Ui", "Ri", "U", "R", "U", "Ri", "U", "R", "Ui", "Ri", "Fi"]
cll41 = ["R2", "Di", "R", "U2", "Ri", "D", "R", "U2", "R"]
cll42 = ["Ui", "F", "R", "U", "Ri", "Ui", "Fi"]

cll_group1 = [cll1, cll2, cll3, cll4, cll5, cll6, cll25, cll26, cll27, cll28, cll29, cll30]
cll_group2 = [cll7, cll8, cll9, cll10, cll19, cll20, cll21, cll22, cll23, cll24, cll17, cll18]
cll_group3 = [cll11, cll12, cll13, cll14, cll15, cll16, cll31, cll32, cll33, cll34, cll35,
               cll36, cll37, cll38, cll39, cll40, cll41, cll42]

def opposit_side(side):
    if side == "y": return "w"
    if side == "w": return "y"
    if side == "b": return "g"
    if side == "g": return "b"
    if side == "r": return "o"
    if side == "o": return "r"

def reverse_alg(alg):
    alg = list(reversed(alg))
    for i in range(6):
        for j in range(len(alg)):
            if alg[j] == normal_moves[i]:
                alg[j] = inverted_moves[i]
            elif alg[j] == inverted_moves[i]:
                alg[j] = normal_moves[i]
    return alg

def correct_alg(alg):
    for i in range(len(alg)//2):
        for i in range(len(alg) - 1):
            for j in range(6):
                if alg[i] == normal_moves[j] and alg[i + 1] == inverted_moves[j]:
                    del alg[i:i + 2]
                    break
            else:
                continue
            break
        for i in range(len(alg) - 1):
            for j in range(6):
                if alg[i] == inverted_moves[j] and alg[i + 1] == normal_moves[j]:
                    del alg[i:i + 2]
                    break
            else:
                continue
            break
    return alg



def rotate_left(alg):
    for i in range(len(alg)):
        if alg[i] == "R":
            alg[i] = "F"
        elif alg[i] == "Ri":
            alg[i] = "Fi"
        elif alg[i] == "R2":
            alg[i] = "F2"

        elif alg[i] == "F":
            alg[i] = "L"
        elif alg[i] == "Fi":
            alg[i] = "Li"
        elif alg[i] == "F2":
            alg[i] = "L2"

        elif alg[i] == "L":
            alg[i] = "B"
        elif alg[i] == "Li":
            alg[i] = "Bi"
        elif alg[i] == "L2":
            alg[i] = "B2"

        elif alg[i] == "B":
            alg[i] = "R"
        elif alg[i] == "Bi":
            alg[i] = "Ri"
        elif alg[i] == "B2":
            alg[i] = "R2"
    return alg

def is_l_before_r_after_index(myalg, index):
    for j in range(index+1, len(myalg)):
        if myalg[j] in ["L", "Li", "L2"]:
            return True
        elif myalg[j] in ["R", "Ri", "R2"]:
            return False
    return False

def spell_alg(alg, short_version=False):
    while any(elem in alg for elem in ["B", "Bi", "B2", "Y", "X"]):
        for i in range(len(alg)):
            if alg[i] in ["B", "Bi", "B2"]:
                index = i
                if is_l_before_r_after_index(alg, index):
                    for _ in range(3):
                        alg.insert(index, "Y")
                else:
                    alg.insert(index, "Y")
                break

        for k in range(len(alg)):
            if alg[k] == "Y":
                alg[k] = "y"
                for i in range(k+1, len(alg)):
                    if alg[i] == "R":
                        alg[i] = "F"
                    elif alg[i] == "Ri":
                        alg[i] = "Fi"
                    elif alg[i] == "R2":
                        alg[i] = "F2"

                    elif alg[i] == "L":
                        alg[i] = "B"
                    elif alg[i] == "Li":
                        alg[i] = "Bi"
                    elif alg[i] == "L2":
                        alg[i] = "B2"

                    elif alg[i] == "B":
                        alg[i] = "R"
                    elif alg[i] == "Bi":
                        alg[i] = "Ri"
                    elif alg[i] == "B2":
                        alg[i] = "R2"

                    elif alg[i] == "F":
                        alg[i] = "L"
                    elif alg[i] == "Fi":
                        alg[i] = "Li"
                    elif alg[i] == "F2":
                        alg[i] = "L2"

            elif alg[k] == "X":
                alg[k] = "x"
                for i in range(k+1, len(alg)):
                    if alg[i] == "F":
                        alg[i] = "U"
                    elif alg[i] == "Fi":
                        alg[i] = "Ui"
                    elif alg[i] == "F2":
                        alg[i] = "U2"

                    elif alg[i] == "D":
                        alg[i] = "F"
                    elif alg[i] == "Di":
                        alg[i] = "Fi"
                    elif alg[i] == "D2":
                        alg[i] = "F2"

                    elif alg[i] == "B":
                        alg[i] = "D"
                    elif alg[i] == "Bi":
                        alg[i] = "Di"
                    elif alg[i] == "B2":
                        alg[i] = "D2"

                    elif alg[i] == "U":
                        alg[i] = "B"
                    elif alg[i] == "Ui":
                        alg[i] = "Bi"
                    elif alg[i] == "U2":
                        alg[i] = "B2"


    strinput = ''.join(alg)
    if short_version:
        string_alg = str(alg)
        if "'y', 'y', 'y', " in string_alg:
            string_alg = string_alg.replace("'y', 'y', 'y', ", "'yi', ")
        return string_alg

    else:
        formatted_str = ""
        for i, char in enumerate(strinput):
            if char.isupper() and formatted_str:
                formatted_str += " "
            if char == "i":
                char = "'"
            if char in ["x", "y"]:
                char = "\033[32m" + char + "\033[0m"
            if char in ["2", "'", "R", "F", "L", "D", "B", "U"] and i < len(strinput) - 1 and strinput[i + 1] in ["x", "y"]:
                char += " "
            formatted_str += char


        formatted_str = formatted_str.replace(" | ", "\n")
        formatted_str = formatted_str.replace("y\033[0m\033[32my\033[0m\033[32my", "y'")
        formatted_str = formatted_str.replace("\033[32my\033[0m\033[32my\033[0m\033[32my\033[0m\033[32my\033[0m", "")
        formatted_str = formatted_str.replace(" \033[32my\033[0m\033[32my'\033[0m ", "")

        caps = sum(1 for c in formatted_str if c.isupper())
        rotations = sum(1 for c in formatted_str if c in ["x", "y"])
        twos = sum(1 for c in formatted_str if c == '2')

        return [formatted_str, caps + twos, rotations]


def scramble(number_of_turns, allowed_moves = possible_moves):
    return [random.choice(allowed_moves) for _ in range(number_of_turns)]

def pair_insertion():
    random_alg = scramble(1, ["R", "Ri", "L", "Li", "F", "Fi", "B", "Bi"])
    random_alg += scramble(1, ["U", "Ui"])
    random_alg += reverse_alg(random_alg[0:1])
    return random_alg

def extended_pair_insertion():
    random_alg = scramble(1, ["R", "Ri", "L", "Li", "F", "Fi", "B", "Bi"])
    random_alg += scramble(1, ["U2", "U", "Ui"])
    random_alg += reverse_alg(random_alg[0:1])
    return random_alg

def count_moves(lst):
    count = 0
    for elem in lst:
        if any(char in elem for char in ['R', 'L', 'D', 'U', 'B', 'F', 'M']):
            count += 1
        if '2' in elem:
            count += 1

def alg_list(alg):
    a = alg.copy()
    b = rotate_left(alg)
    c = rotate_left(b.copy())
    d = rotate_left(c.copy())
    return [a, b, c, d]


def on_which_side(pos):
    if pos in white_side:
        return "w"
    elif pos in yellow_side:
        return "y"
    elif pos in orange_side:
        return "o"
    elif pos in red_side:
        return "r"
    elif pos in blue_side:
        return "b"
    elif pos in green_side:
        return "g"