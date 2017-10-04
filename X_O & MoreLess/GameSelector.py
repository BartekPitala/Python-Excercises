import Board
import MoreLess


class GameSelector:
    def __init__(self):
        print("\nWelcome to my leisure centre! Please, choose the game You wish to play:")
        print(10 * "=" + " GAME SELECTION " + 10 * "=")
        print("\"1\" for Tick-Tack-Toe\n\"2\" for More-Less")
        self.game = None

    def PlayXO(self , size):
        self.game = Board.Board(size)

    def PlayMoreLess(self , value):
        self.game = MoreLess.MoreLess(value)


