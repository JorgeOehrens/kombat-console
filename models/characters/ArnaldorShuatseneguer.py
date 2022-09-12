from models.characters.Character import Character
from models.movements.SpecialAttack import Taladoken2, Remuyuken2
from models.movements.BasicAttack import Arriba, Abajo, Derecha, Izquierda, Puño, Patada



class ArnoldShuatseneguer(Character):

    def __init__(self):
        super().__init__("Arnold Shuatseneguer", 6, [Arriba(), Abajo(), Derecha(), Izquierda()]  , [Taladoken2(),Remuyuken2()] , [Puño(), Patada()] )


