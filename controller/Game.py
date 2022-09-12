
from models.characters.Tonynstallone import TonynStallone
from models.characters.ArnaldorShuatseneguer import ArnoldShuatseneguer
from models.characters.Character import Character
from rx.subject import Subject
from models.events.Event import Event
from models.movements.Movement import Movement


class Game:
    def __init__(self, player1: 'Character', player2: 'Character'):
        self.player1Disposable = self.player1.eventNow.subscribe()
        self.player2Disposable = self.player2.eventNow.subscribe()

        player1Movement=[]
        player2Movement=[]

        player1A=[]
        player2Attack=[]

        self.result: Subject[bool]= Subject()

        self.nextMovement: Subject[str]= Subject()

    def freeMemory(self) -> None:
        self.player1Disposable.dipose()
        self.player2Disposable.dipose()

    def winner(self) -> None:
        self.freeMemory()
        self.result.on_next(True)
        self.result.on_completed()

    def acceptEvent(self, event: 'Event') -> None:
        event.visitGame(self)

    def createJsonGame(self) -> None:
        pass

    def figthInteraction(self, playerAttack: 'Character', playerReceive: 'Character', movement: 'Movement') -> str:
        playerAttack.attack(playerReceive, movement)


        return "{} recibió daño".format(playerReceive.__str__())



