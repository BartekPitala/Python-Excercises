class Board:
    def __init__(self, size):
        self.size = size
        self.tab = [["-" for i in range(size)] for j in range(size)]
        self.turns = 0
        self.winner_found = False
        print("Welcome to the Tick-Tack-Toe game!\nYour task is to fill whole row, column or diagonal with Your sign before the computer does it.")
        print("You and the computer take turns one after the other")
        print("Good Luck and let us start!")

    def DrawBoard(self):
        print(25 * "=")
        for i in range(self.size):
            print("||" , end = "")
            for j in range(self.size):
                print(" " + self.tab[i][j] + " |" , end = "")
            print("|\n", end = "")
        print(25 * "=")


    def PutSign(self , x , y , mark):
        if x >= 0 and x < self.size and y >= 0 and y < self.size:
            if self.tab[x][y] == "-":
                self.turns += 1
                self.tab[x][y] = mark
                return True
            else:
                print("This place is already taken. Choose different coordinates:\n")
                return False
        else:
            print ("Given coordinates out of board range. Choose proper coordinates\n")
            return False

    def CheckComputerCoords(self , x , y):
        if x >= 0 and x < self.size and y >= 0 and y < self.size:
            if self.tab[x][y] == "-":
                return True
            else:
                return False
        else:
            return False

    def CheckRow(self):
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.tab[i][j] == "X":
                    count +=1
                elif self.tab[i][j] == "O":
                    count -= 1
            if count == self.size or count == -self.size:
                self.winner_found = True
        return self.winner_found

    def CheckCol(self):
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.tab[j][i] == "X":
                    count +=1
                elif self.tab[j][i] == "O":
                    count -= 1
            if count == self.size or count == -self.size:
               self.winner_found = True
        return self.winner_found

    def CheckMainDiagon(self):
        count = 0
        for i in range(self.size):
               if self.tab[i][i] == "X":
                   count += 1
               elif self.tab[i][i] == "O":
                   count -= 1
        if count == self.size or count == -self.size:
            self.winner_found= True
        return self.winner_found

    def CheckSecondaryDiagon(self):
        count = 0
        for i in range(self.size):
            if self.tab[i][self.size - i - 1] == "X":
                count += 1
            elif self.tab[i][self.size - i - 1] == "O":
                count -= 1
        if count == self.size or count == -self.size:
            self.winner_found = True
        return self.winner_found
