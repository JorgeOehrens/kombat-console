from models.characters.Tonynstallone import TonynStallone
from models.characters.Character import Character
from models.movements.BasicAttack import Puño, Patada
from models.characters.ArnaldorShuatseneguer import ArnoldShuatseneguer
import json


def RecibeDanage(playerAttack: 'Character' ):
    player1=playerAttack

    player2= TonynStallone()

    lifeNow= player2.energyNow

    player2.eventNow.subscribe(
        lambda event: print(event)
    )

    for a in range(7):
        playerAttack.attack(player2, Puño())
        playerAttack.attack(player1, Puño())


    assert player2.energyNow < lifeNow

def readJson():

    f = open("../view/Fight/fight1.json", "r")
    content = f.read()

    jsondecoded = json.loads(content)
    player1=jsondecoded["player1"]
    player2=jsondecoded["player2"]

    player1Movements=player1["movimientos"]
    player1Attack= player1["golpes"]


    player2Movements=player2["movimientos"]
    player2Attack= player2["golpes"]

    listaPlayer1=player1Attack+player1Movements
    joinList="".join(listaPlayer1)
    ValueListPlayer1=len(joinList)

    listaPlayer2 = player2Attack + player2Movements
    joinList = "".join(listaPlayer2)
    ValueListPlayer2 = len(joinList)


def tests():
    RecibeDanage(ArnoldShuatseneguer())
    readJson()