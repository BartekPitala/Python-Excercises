import random
class MoreLess():
    def __init__(self , value):
        self.step_counter = 0
        self.range = value
        self.number = random.randint(0 , self.range)
        print("Welcome to the More-Less game! \nYour task is to find the number I chose from range [0 , " + str(self.range) + "]")
        print("Each time You make a decision, I will tell You if my number is greater or smaller than Your prediction.")
        print("We will see how quick can You guess my choice.")
        print("Good Luck and let us start!")

    def Compare(self , value):
        self.step_counter += 1
        if value > self.number:
            print("Ooops! My number is SMALLER than You thought... Try again!")
            return False
        elif value < self.number:
            print("Ooops! My number is GREATER than You thought... Try again!")
            return False
        elif value == self.number:
            print("YES!! That is exactly the number I chose! Congratulations. You found it in " + str(self.step_counter) + " steps.")
            return True
