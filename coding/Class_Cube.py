import random
import numpy as np
import matplotlib.pyplot as plt



class Cube:
    def __init__(self, cp, rotationlist = [], cr = ["Y", "B", "R", "G", "O", "W"], mturns = 0, solved_pos = range(0,48), rel_op = range(0,48)):
        self.cp = cp
        self.cr = cr
        self.solved_pos = solved_pos
        self.rel_op = rel_op
        self.rotationlist = rotationlist







    def reset(self):
        self.cp = op
        self.rotationlist = []

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
        self.rotationlist += ["y"]
        print("I changed the rotationlist")
        """self.cp = [self.cp[3], self.cp[0], self.cp[1], self.cp[2], self.cp[8], self.cp[9], self.cp[10], self.cp[11],
                   self.cp[12], self.cp[13], self.cp[15], self.cp[14], self.cp[16], self.cp[17], self.cp[18],
                   self.cp[19], self.cp[4], self.cp[5], self.cp[7], self.cp[6], self.cp[21], self.cp[23], self.cp[20],
                   self.cp[22], self.cp[27], self.cp[24], self.cp[25], self.cp[26], self.cp[32], self.cp[33],
                   self.cp[34], self.cp[35], self.cp[36], self.cp[37], self.cp[38], self.cp[39], self.cp[40],
                   self.cp[41], self.cp[42], self.cp[43], self.cp[28], self.cp[29], self.cp[30], self.cp[31],
                   self.cp[45], self.cp[46], self.cp[47], self.cp[44]]
        self.cr = [self.cr[0], self.cr[2], self.cr[3], self.cr[4], self.cr[1], self.cr[5]]
        self.solved_pos = [self.solved_pos[3], self.solved_pos[0], self.solved_pos[1], self.solved_pos[2],
                           self.solved_pos[8], self.solved_pos[9], self.solved_pos[10], self.solved_pos[11],
                           self.solved_pos[12], self.solved_pos[13], self.solved_pos[15], self.solved_pos[14],
                           self.solved_pos[16], self.solved_pos[17],self.solved_pos[18], self.solved_pos[19],
                           self.solved_pos[4], self.solved_pos[5], self.solved_pos[7], self.solved_pos[6],
                           self.solved_pos[21], self.solved_pos[23], self.solved_pos[20], self.solved_pos[22],
                           self.solved_pos[27], self.solved_pos[24], self.solved_pos[25], self.solved_pos[26],
                           self.solved_pos[32], self.solved_pos[33], self.solved_pos[34], self.solved_pos[35],
                           self.solved_pos[36], self.solved_pos[37], self.solved_pos[38], self.solved_pos[39],
                           self.solved_pos[40], self.solved_pos[41], self.solved_pos[42], self.solved_pos[43],
                           self.solved_pos[28], self.solved_pos[29], self.solved_pos[30], self.solved_pos[31],
                           self.solved_pos[45], self.solved_pos[46], self.solved_pos[47], self.solved_pos[44]]
        for _ in range(3):
            self.rel_op = [self.rel_op[3], self.rel_op[0], self.rel_op[1], self.rel_op[2],
                           self.rel_op[8], self.rel_op[9], self.rel_op[10], self.rel_op[11],
                           self.rel_op[12], self.rel_op[13], self.rel_op[15], self.rel_op[14],
                           self.rel_op[16], self.rel_op[17], self.rel_op[18], self.rel_op[19],
                           self.rel_op[4], self.rel_op[5], self.rel_op[7], self.rel_op[6],
                           self.rel_op[21], self.rel_op[23], self.rel_op[20], self.rel_op[22],
                           self.rel_op[27], self.rel_op[24], self.rel_op[25], self.rel_op[26],
                           self.rel_op[32], self.rel_op[33], self.rel_op[34], self.rel_op[35],
                           self.rel_op[36], self.rel_op[37], self.rel_op[38], self.rel_op[39],
                           self.rel_op[40], self.rel_op[41], self.rel_op[42], self.rel_op[43],
                           self.rel_op[28], self.rel_op[29], self.rel_op[30], self.rel_op[31],
                           self.rel_op[45], self.rel_op[46], self.rel_op[47], self.rel_op[44]]"""

    def xturn(self):
        self.rotationlist += ["x"]

        """self.cp = [self.cp[8], self.cp[9], self.cp[10], self.cp[11], self.cp[5], self.cp[6], self.cp[7], self.cp[4], self.cp[20],
                   self.cp[21], self.cp[23], self.cp[22], self.cp[14], self.cp[12], self.cp[15], self.cp[13], self.cp[2], self.cp[3],
                   self.cp[1], self.cp[0], self.cp[19], self.cp[18], self.cp[17], self.cp[16], self.cp[32], self.cp[33], self.cp[34],
                   self.cp[35], self.cp[29], self.cp[30], self.cp[31], self.cp[28], self.cp[44], self.cp[45], self.cp[46], self.cp[47],
                   self.cp[39], self.cp[36], self.cp[37], self.cp[38], self.cp[26], self.cp[27], self.cp[24], self.cp[25], self.cp[42],
                   self.cp[43], self.cp[40], self.cp[41]]
        self.cr = [self.cr[2], self.cr[1], self.cr[5], self.cr[3], self.cr[0], self.cr[4]]

        self.solved_pos = [self.solved_pos[8], self.solved_pos[9], self.solved_pos[10], self.solved_pos[11],
                           self.solved_pos[5], self.solved_pos[6], self.solved_pos[7], self.solved_pos[4],
                           self.solved_pos[20], self.solved_pos[21], self.solved_pos[23], self.solved_pos[22],
                           self.solved_pos[14], self.solved_pos[12], self.solved_pos[15], self.solved_pos[13],
                           self.solved_pos[2], self.solved_pos[3], self.solved_pos[1], self.solved_pos[0],
                           self.solved_pos[19], self.solved_pos[18], self.solved_pos[17], self.solved_pos[16],
                           self.solved_pos[32], self.solved_pos[33], self.solved_pos[34], self.solved_pos[35],
                           self.solved_pos[29], self.solved_pos[30], self.solved_pos[31], self.solved_pos[28],
                           self.solved_pos[44], self.solved_pos[45], self.solved_pos[46], self.solved_pos[47],
                           self.solved_pos[39], self.solved_pos[36], self.solved_pos[37], self.solved_pos[38],
                           self.solved_pos[26], self.solved_pos[27], self.solved_pos[24], self.solved_pos[25],
                           self.solved_pos[42], self.solved_pos[43], self.solved_pos[40], self.solved_pos[41]]

        for _ in range(3):
            self.rel_op = [self.rel_op[8], self.rel_op[9], self.rel_op[10], self.rel_op[11],
                           self.rel_op[5], self.rel_op[6], self.rel_op[7], self.rel_op[4],
                           self.rel_op[20], self.rel_op[21], self.rel_op[23], self.rel_op[22],
                           self.rel_op[14], self.rel_op[12], self.rel_op[15], self.rel_op[13],
                           self.rel_op[2], self.rel_op[3], self.rel_op[1], self.rel_op[0],
                           self.rel_op[19], self.rel_op[18], self.rel_op[17], self.rel_op[16],
                           self.rel_op[32], self.rel_op[33], self.rel_op[34], self.rel_op[35],
                           self.rel_op[29], self.rel_op[30], self.rel_op[31], self.rel_op[28],
                           self.rel_op[44], self.rel_op[45], self.rel_op[46], self.rel_op[47],
                           self.rel_op[39], self.rel_op[36], self.rel_op[37], self.rel_op[38],
                           self.rel_op[26], self.rel_op[27], self.rel_op[24], self.rel_op[25],
                           self.rel_op[42], self.rel_op[43], self.rel_op[40], self.rel_op[41]]"""

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
        "x": lambda self: self.xturn(),
        "xi": lambda self: self.xiturn(),
        "x2": lambda self: self.x2turn(),
        "y": lambda self: self.yturn(),
        "yi": lambda self: self.yiturn(),
        "y2": lambda self: self.y2turn()
    }


    def doalg(self, alg):

        #print("the alg is:", alg)
        #print("rotationlist is:", self.rotationlist)

        for l in range(len(self.rotationlist)):
            if self.rotationlist[l] == "y":
                for i in range(len(alg)):
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

            elif self.rotationlist[l] == "x":
                for i in range(len(alg)):
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



        for k in range(len(alg)):
            if alg[k] == "y":
                self.rotationlist += ["y"]
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

            elif alg[k] == "x":
                self.rotationlist += ["x"]
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

            else:
                self.move_dict[alg[k]](self)





    def virtualcube(self):
        pos = self.cp
        for rotation in self.rotationlist:
            if rotation == "x":
                pass

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

class Alg:


    def __init__(self, alg):
        self.alg = alg

    def reverse(self):
        self.alg = list(reversed(self.alg))  # read the alg backwards
        for i in range(6):  # every inverted turn gets normal and vice versa
            for j in range(len(self.alg)):
                if self.alg[j] == normal_moves[i]:
                    self.alg[j] = inverted_moves[i]
                elif self.alg[j] == inverted_moves[i]:
                    self.alg[j] = normal_moves[i]
        return self.alg

    def correct(self):  # cancels out moves and simplifies the alg...
        while True:
            old_hard_alg = self.alg.copy()
            for m in range(6):
                changed2 = True
                while changed2:
                    changed2 = False
                    i = 0
                    while i < len(self.alg) - 1:
                        if self.alg[i] == normal_moves[m] and self.alg[i + 1] == inverted_moves[m] \
                                or self.alg[i] == inverted_moves[m] and self.alg[i + 1] == normal_moves[m] \
                                or self.alg[i] == double_moves[m] and self.alg[i + 1] == double_moves[m]:
                            del self.alg[i:i + 2]
                            changed2 = True
                        elif self.alg[i] == double_moves[m] and self.alg[i + 1] == normal_moves[m] \
                                or self.alg[i] == normal_moves[m] and self.alg[i + 1] == double_moves[m]:
                            self.alg[i:i + 2] = [inverted_moves[m]]
                            changed2 = True
                        elif self.alg[i] == double_moves[m] and self.alg[i + 1] == inverted_moves[m] \
                                or self.alg[i] == inverted_moves[m] and self.alg[i + 1] == double_moves[m]:
                            self.alg[i:i + 2] = [normal_moves[m]]
                            changed2 = True
                        elif self.alg[i] == normal_moves[m] and self.alg[i + 1] == normal_moves[m] \
                                or self.alg[i] == inverted_moves[m] and self.alg[i + 1] == inverted_moves[m]:
                            self.alg[i:i + 2] = [double_moves[m]]
                            changed2 = True
                        else:
                            i += 1
            if self.alg == old_hard_alg:
                break

        return self.alg



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

    # alg123 = Alg(['Ui', 'L', 'U', 'R', 'Ui', 'Li', 'U', 'Ri', 'Ui', 'L', 'Ui'])
    # alg234 = Alg(list(alg123.alg))  # create a copy of alg123 and assign it to alg234







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
normal_moves = ["R", "U", "F", "L", "B", "D"]
inverted_moves = ["Ri", "Ui", "Fi", "Li", "Bi", "Di"]
double_moves = ["R2", "U2", "F2", "L2", "B2", "D2"]
possible_moves = normal_moves + inverted_moves
cube1 = Cube(op)
helpcube = Cube(op)


sexymove = ["R","U","Ri","Ui"]
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
tperm = ["R", "U", "Ri", "Ui", "Ri", "F", "R2", "Ui", "Ri", "Ui", "R", "U", "Ri", "Fi"]






def reverse_alg(alg):
    alg = list(reversed(alg))                      #read the alg backwards
    for i in range(6):                             #every inverted turn gets normal and vice versa
        for j in range(len(alg)):
            if alg[j] == normal_moves[i]:
                alg[j] = inverted_moves[i]
            elif alg[j] == inverted_moves[i]:
                alg[j] = normal_moves[i]
    return alg

def correct_alg(alg): #this only kicks out normal moves followed by inverted ones and vice versa...
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

def mirror_alg(alg):
    for i in range(len(alg)):
        if alg[i] == "U":
            alg[i] = "Ui"
        elif alg[i] == "Ui":
            alg[i] = "U"
        elif alg[i] == "D":
            alg[i] = "Di"
        elif alg[i] == "Di":
            alg[i] = "D"
        elif alg[i] == "R":
            alg[i] = "Li"
        elif alg[i] == "Li":
            alg[i] = "R"
        elif alg[i] == "L":
            alg[i] = "Ri"
        elif alg[i] == "Ri":
            alg[i] = "L"
        elif alg[i] == "R2":
            alg[i] = "L2"
        elif alg[i] == "L2":
            alg[i] = "R2"
        elif alg[i] == "F":
            alg[i] = "Fi"
        elif alg[i] == "Fi":
            alg[i] = "F"
        elif alg[i] == "B":
            alg[i] = "Bi"
        elif alg[i] == "Bi":
            alg[i] = "B"
    return alg + ["mirror"]

def rotate_left(alg):
    for i in range(len(alg)):
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
            alg[i] = "B"
        elif alg[i] == "B":
            alg[i] = "R"
        elif alg[i] == "Bi":
            alg[i] = "Ri"
        elif alg[i] == "B2":
            alg[i] = "R2"
    return alg + ["rotate_left"]

def spell_alg(alg):
    for k in range(len(alg)):
        if alg[k] == "y":
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
        elif alg[k] == "x":
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
    formatted_str = ""  # neu definieren
    for char in strinput:
        if char.isupper() and formatted_str:
            formatted_str += " "
        if char == "i":
            char = "'"
        formatted_str += char

    return formatted_str

def scramble(number_of_turns, allowed_moves = possible_moves):
    return [random.choice(allowed_moves) for _ in range(number_of_turns)]

def check_common_elements(list1, list2):
    common_elements = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            common_elements += 1
    return common_elements

def mark_equal_elements_of_two_lists(compare_list, list):
    print("\033[0m", compare_list, sep="")
    print("\033[0m[", end="")
    for i in range(48):
        if compare_list[i] == list[i]:
            if i == 47:
                print(f"\033[32m{list[i]}\033[0m]")
            else:
                print(f"\033[32m{list[i]}\033[0m, ", end="")
        else:
            if i == 47:
                print(f"{list[i]}]")
            else:
                print(f"{list[i]}, ", end="")
    print("correct_stickers =", check_common_elements(compare_list, list))





"""
cube1.doalg(["R2", "y"])
cube1.doalg(["F2"])
cube1.doalg(["F"])
cube1.doalg(["y"]*3 +["R"])
cube1.doalg(["D2"])
cube1.virtualcube()
"""

"""myalg = ["R2", "y", "R2"]
print(myalg)
print(spell_alg(myalg))
"""