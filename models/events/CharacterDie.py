from models.events.Event import Event
from controller.Game import *

class CharacterDie(Event):

    def visitGame(self, game: 'Game'):
        game.gameOver()

        