from models.characters.Character import Character
from models.movements.SpecialAttack import Taladoken, Remuyuken 
from models.movements.BasicAttack import Arriba, Abajo, Derecha, Izquierda, Puño, Patada


class TonynStallone(Character):

    def __init__(self):
        super().__init__("Tony n' Stallone", 6, [Arriba(), Abajo(), Derecha(), Izquierda()]  , [Taladoken(),Remuyuken()] , [Puño(), Patada()] )
        

