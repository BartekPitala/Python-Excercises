from Board import Board
from GameSelector import GameSelector
from MoreLess import MoreLess
import random


if __name__ == "__main__":
    game = GameSelector()
    choice = 0
    while not (choice == "1" or choice == "2"):
        choice = input("Your choice: ")
    if choice == "1":
        size = int(input("Please enter the size of the board You wish to play on as a number between 3 and 10 (mind You, board is a square): "))
        while(size > 10 or size < 3):
            size = int(input("The size You entered is wrong...Please, enter the correct size - a number between 3 and 10: "))
        game.PlayXO(size)
        game.game.DrawBoard()

        print("Your sign is a \"X\".")
        while not game.game.winner_found:
            print("YOUR turn")
            x = input("Insert X-axis coordinate (0 - leftmost column , " + str(game.game.size - 1) +" - rightmost column): ")
            y = input("Insert Y-axis coordinate (0 - uppermost row, " + str(game.game.size - 1) +" - lowermost row): ")
            while not game.game.PutSign(int(x) , int(y) , "X"):
                x = input("Insert X-axis coordinate (0 - leftmost column , " + str(game.game.size - 1) + " - rightmost column): ")
                y = input("Insert Y-axis coordinate (0 - uppermost row, " + str(game.game.size - 1) + " - lowermost row): ")
            game.game.DrawBoard()

            game.game.CheckRow()
            game.game.CheckCol()
            game.game.CheckMainDiagon()
            game.game.CheckSecondaryDiagon()

            if game.game.winner_found:
                print("Congrats! You won!")
                break

            print("COMPUTER's turn:\n")
            x = random.randint(0 , game.game.size - 1)
            y = random.randint(0 , game.game.size - 1)
            while not game.game.CheckComputerCoords(x , y):
                x = random.randint(0, game.game.size - 1)
                y = random.randint(0, game.game.size - 1)
            game.game.PutSign(x , y , "O")
            game.game.DrawBoard()

            game.game.CheckRow()
            game.game.CheckCol()
            game.game.CheckMainDiagon()
            game.game.CheckSecondaryDiagon()

            if game.game.winner_found:
                print("Ooops! You lost... Computer is the winner :(")
                break


    if choice == "2":
        val = int(input("Choose the maximum range of More-Less value: "))
        game.PlayMoreLess(val)
        number = int(input("Type a number You think I have chosen(integer): "))
        while not game.game.Compare(number):
            number = int(input("Type a number You think I have chosen(integer): "))

