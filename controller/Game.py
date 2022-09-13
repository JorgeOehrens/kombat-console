
from models.characters.Character import *
from rx.subject import Subject
from models.events.Event import *
from models.movements.Movement import *
import json
from typing import List
from models.movements.BasicAttack import *
from models.movements.SpecialAttack import *

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

        lifeNowPlayer1 = self.player1.energyNow
        lifeNowPlayer2 = self.player2.energyNow


        player2.eventNow.subscribe(
            lambda event: print(event)
        )
        player1.eventNow.subscribe(
            lambda event: print(event)
        )


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
                    movement = player1Movements[c2]
                    attack = player1Attack[c2]
                    combination = movement + attack
                    if combination == "SDK":
                        print(self.player1.name, 'conecta un', Action.REMUYUKEN.description())
                        self.player1.attack(self.player2, Remuyuken())

                    elif combination == "DSDP":
                        print(self.player1.name, 'conecta un', Action.TALADOKEN.description())
                        self.player1.attack(self.player2, Taladoken())

                    else:
                        if movement == "W":
                            str = self.player1.name + ' salta '
                        elif movement == "S":
                            str = self.player1.name + ' se agacha'
                        elif movement == "A":
                            str = self.player1.name + ' avanza a la izquierda'
                        else:
                            str = self.player1.name + ' avanza a la derecha'

                        if attack == "P":
                            str = str + ' y golpea'
                            self.player1.attack(self.player2, Puño())

                        elif attack == "K":
                            str = str + ' y patea'
                            self.player1.attack(self.player2, Patada())

                        else:
                            str = str
                        print(str)
                    firstPlayer = self.player2

                    c2 += 1

                else:
                    movement = player2Movements[c]
                    attack = player2Attack[c]
                    combination = movement + attack
                    if combination == "SAK":
                        print(self.player2.name, 'conecta un', Action.REMUYUKEN2.description())
                        self.player2.attack(self.player1, Remuyuken2())

                    elif combination == "ASAP":
                        print(self.player2.name, 'conecta un', Action.TALADOKEN2.description())
                        self.player2.attack(self.player1, Taladoken2())

                    else:
                        if movement == "W":
                            str = self.player2.name + ' salta '
                        elif movement == "S":
                            str = self.player2.name + ' se agacha'
                        elif movement == "A":
                            str = self.player2.name + ' avanza a la izquierda'
                        else:
                            str = self.player2.name + ' avanza a la derecha'

                        if attack == "P":
                            str = str + ' y golpea'
                            self.player2.attack(self.player1, Puño())

                        elif attack == "K":
                            str = str + ' y patea'
                            self.player2.attack(self.player1, Patada())

                        print(str)
                    c += 1
                    firstPlayer = self.player1


        else:
            print('Parte ', self.player2.name)
            c=0
            c2=0
            firstPlayer=self.player2
            while self.player1.energyNow != 0 or self.player1.energyNow != 0:

                if firstPlayer == self.player2:
                    movement = player2Movements[c]
                    attack = player2Attack[c]
                    combination = movement + attack
                    if combination == "SAK":
                        print(self.player2.name, 'conecta un' ,Action.REMUYUKEN2.description())
                        self.player2.attack(self.player1,Remuyuken2())

                    elif combination == "ASAP":
                        print(self.player2.name, 'conecta un' ,Action.TALADOKEN2.description())
                        self.player2.attack(self.player1,Taladoken2())

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
                            self.player2.attack(self.player1,Puño())

                        elif attack == "K":
                            str= str + ' y patea'
                            self.player2.attack(self.player1, Patada())

                        print(str)
                    c+=1
                    firstPlayer=self.player1







                else:
                    movement = player1Movements[c2]
                    attack = player1Attack[c2]
                    combination = movement + attack
                    if combination == "SDK":
                        print(self.player1.name, 'conecta un', Action.REMUYUKEN.description())
                        self.player1.attack(self.player2,Remuyuken())

                    elif combination == "DSDP":
                        print(self.player1.name, 'conecta un', Action.TALADOKEN.description())
                        self.player1.attack(self.player2,Taladoken())

                    else:
                        if movement == "W":
                            str = self.player1.name + ' salta '
                        elif movement == "S":
                            str = self.player1.name + ' se agacha'
                        elif movement == "A":
                            str = self.player1.name + ' avanza a la izquierda'
                        else:
                            str = self.player1.name + ' avanza a la derecha'

                        if attack == "P":
                            str = str + ' y golpea'
                            self.player1.attack(self.player2,Puño())

                        elif attack == "K":
                            str = str + ' y patea'
                            self.player1.attack(self.player2, Patada())

                        else:
                            str=str
                        print(str)
                    firstPlayer = self.player2

                    c2+=1








