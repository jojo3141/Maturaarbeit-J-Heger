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






normal_moves = ["R", "U", "F", "L", "B", "D"]
inverted_moves = ["Ri", "Ui", "Fi", "Li", "Bi", "Di"]
double_moves = ["R2", "U2", "F2", "L2", "B2", "D2"]

alg123 = Alg(['Ui', 'L', 'U', 'R', 'Ui', 'Li', 'U', 'Ri', 'Ui', 'L', 'Ui'])
#alg234 = Alg(list(alg123.alg))  # create a copy of alg123 and assign it to alg234

