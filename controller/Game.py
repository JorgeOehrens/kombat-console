
from models.characters.Character import Character




class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):

        print("Game.start()")

        while self.player1.isAlive() and self.player2.isAlive():

            self.player1.attack(self.player2)
            self.player2.attack(self.player1)

            print(self.player1)
            print(self.player2)

        if self.player1.isAlive():
            print(self.player1.name + " is the winner")
        else:
            print(self.player2.name + " is the winner")

    def __str__(self):
        return "Game: " + self.player1.name + " vs " + self.player2.name
        




