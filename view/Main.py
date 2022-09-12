from controller.Game import Game
from models.characters.Tonynstallone import TonynStallone
from models.characters.ArnaldorShuatseneguer import ArnoldShuatseneguer

class Main:
    def __init__(self):

        self.game= Game(TonynStallone(), ArnoldShuatseneguer())


if __name__ == '__main__':
    print("Bienvenido a desafio Talana")
    