
from models.characters.Character import *
from rx.subject import Subject
from models.events.Event import *
from models.movements.Movement import *
import json
from typing import List

from view.Action import Action
class Game:
    def __init__(self, player1: 'Character', player2: 'Character', battle:json):
        self.player1= player1
        self.player2= player2

        self.player1Disposable = self.player1.eventNow.subscribe()
        self.player2Disposable = self.player2.eventNow.subscribe()

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
            print('Parte ', self.player1.name)
            c=0

            firstPlayer=self.player1
            while self.player1.energyNow != 0 or self.player1.energyNow != 0:

                if firstPlayer == self.player1:
                    movement = player1Movements[c]
                    attack = player1Attack[c]
                    combination = movement + attack
                    if combination == "DSDP":
                        print(Action.REMUYUKEN.description())

                else:
                    movement = player1Movements[c]
                    attack = player1Attack[c]
                    combination = movement + attack
                    print(combination)


        else:
            print('Parte ', self.player2.name)
            c=0
            firstPlayer=self.player2
            while self.player1.energyNow != 0 or self.player1.energyNow != 0:

                if firstPlayer == self.player2:
                    movement = player2Movements[c]
                    attack = player2Attack[c]
                    combination = movement + attack
                    if combination == "SAK":
                        print(self.player2.name, 'conecta un' ,Action.REMUYUKEN2.description())

                    elif combination == "ASAP":
                        print(self.player2.name, 'conecta un' ,Action.TALADOKEN2.description())

                    else:
                        if movement == "W":
                            str=self.player2.name + ' salta '
                        elif movement == "S":
                            str= self.player2.name + ' se agacha'
                        elif movement == "A":
                            str = self.player2.name + ' avanza a la izquierda'
                        else:
                            str = self.player2.name + ' avanza a la derecha'

                        if attack == "P":
                            str= str + ' y golpea'
                        elif attack == "K":
                            str= str + ' y patea'
                        print(str)







                else:
                    movement = player1Movements[c]
                    attack = player1Attack[c]
                    combination = movement + attack
                    print(combination)
                c+=1




    def gameOver(self) -> None:
        self.freeMemory()

        self.gameResult.on_next(False)
        self.gameResult.on_completed()
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




