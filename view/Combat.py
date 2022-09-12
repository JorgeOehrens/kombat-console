from models.characters.Character import Character

from controller.Game import Game

class Combat:
    def __init__(self, game: 'Game',player1: 'Character', player2: 'Character'):
        self.game= game
        self.player1=player1
        self.player2 = player2
        self.fight()

    def fight(self) -> None:
        while self.game.ifLiveCharacter():
            print(' {} esta atacando'.format(self.player1))


    def turnoJugador(self) -> None:

        print(self.jugador.__str__())
        self.optionsActions()

    def optionsActions(self):





