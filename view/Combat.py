from models.characters.Character import Character
from view.Action import Action
from controller.Game import Game
import typing, json
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


    def optionsActions(self)-> 'Action':
        while True:
            listActions : typing.List[Action] = [action for action in Action]
            for action in listActions:
                print(action, "): ", action.description())
                try:
                    action_player = Action.strtToAction(
                        input("Ingrese accion")
                    )
                except ValueError:
                    print ("Accion no permitida")
                else:
                    return action_player






