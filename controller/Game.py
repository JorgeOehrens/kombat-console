
from models.characters.Character import *
from rx.subject import Subject
from models.events.Event import *
from models.movements.Movement import *
import json

class Game:
    def __init__(self, player1: 'Character', player2: 'Character', battle:json):

        self.player1= player1
        self.player2= player2

        self.player1Disposable = self.player1.eventNow.subscribe()
        self.player2Disposable = self.player2.eventNow.subscribe()

        player1Movement=[]
        player2Movement=[]

        player1A=[]
        player2Attack=[]

        self.result: Subject[bool]= Subject()

        self.nextMovement: Subject[str]= Subject()

        self.battle = battle

        content = battle.read()

        jsondecoded = json.loads(content)
        player1 = jsondecoded["player1"]
        player2 = jsondecoded["player2"]

        player1Movements = player1["movimientos"]
        player1Attack = player1["golpes"]

        player2Movements = player2["movimientos"]
        player2Attack = player2["golpes"]

        listaPlayer1 = player1Attack + player1Movements
        joinList = "".join(listaPlayer1)
        ValueListPlayer1 = len(joinList)

        listaPlayer2 = player2Attack + player2Movements
        joinList2 = "".join(listaPlayer2)
        ValueListPlayer2 = len(joinList)

        if ValueListPlayer1 > ValueListPlayer2:
            print ('Parte ' , self.player1.name)
        else:
            print ('Parte ',self.player2.name)
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



    def ifLiveCharacter(self) -> bool:

        if self.player1.energyNow == 0 or self.player2.energyNow == 0:
            return False

        else:
            return True




