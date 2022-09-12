from controller.Game import Game
from models.characters.Tonynstallone import TonynStallone
from models.characters.ArnaldorShuatseneguer import ArnoldShuatseneguer

class Main:
    def __init__(self):

        self.game= Game( TonynStallone(), ArnoldShuatseneguer())

    def start(self) -> None:
        self.combat()
        self.characterWinner()
        self.game.start()




if __name__ == '__main__':
    print("Bienvenid@ a desafío Talana \n\n")
    Main()
