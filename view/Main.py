from view.Combat import Combat
from models.characters.Tonynstallone import *
from models.characters.ArnaldorShuatseneguer import *

from controller.Game import Game

class Main:
    def __init__(self):
        battle = open("Fight/fight1.json", "r")

        self.game= Game( TonynStallone(), ArnoldShuatseneguer(),battle)

    def start(self) -> None:
        self.Combat()
        self.characterWinner()
        self.game.start()




if __name__ == '__main__':
    print("Bienvenid@ a desafío Talana \n\n")
    Main()
