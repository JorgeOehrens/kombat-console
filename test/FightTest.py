from models.characters.Tonynstallone import TonynStallone
from models.characters.Character import Character
from models.movements.BasicAttack import Puño
from models.characters.ArnaldorShuatseneguer import ArnoldShuatseneguer


def RecibeDanage(playerAttack: 'Character' ):

    player2= TonynStallone()

    lifeNow= player2.energyNow

    for a in range(3):
        playerAttack.attack(player2, Puño())

    assert player2.energyNow < lifeNow




def tests():
    RecibeDanage(ArnoldShuatseneguer())