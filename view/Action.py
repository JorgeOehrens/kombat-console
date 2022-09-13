from enum import Enum
from models.characters.Character import *

class Action(Enum):
    ARRIBA= "W"
    ABAJO= "S"
    IZQUIERDA= "A"
    DERECHA= "D"
    PUÑO= "P"
    PATADA= "K"
    TALADOKEN= "DSDP"
    TALADOKEN2= "ASAP"
    REMUYUKEN= "DSDP"
    REMUYUKEN2= "SAK"

    def description(self) -> str:
        if self == self.ARRIBA:
            return "Arriba"
        elif self == self.ABAJO:
            return "Abajo"
        elif self ==  self.IZQUIERDA:
            return "Izquierda"
        elif self == self.DERECHA:
            return "Derecha"
        elif self == self.PUÑO:
            return "Puño"
        elif self == self.PATADA:
            return "Patada"
        elif self == self.TALADOKEN:
            return "Taladoken"
        elif self == self.TALADOKEN2:
            return "Taladoken"
        elif self == self.REMUYUKEN:
            return "Remuyuken"
        elif self == self.REMUYUKEN2:
            return "El jugador Remuyuken"
        else:
            raise Exception("Movimiento no valido")

    def __str__ (self):
        if self == self.ARRIBA:
            return "Arriba"
        elif self == self.ABAJO:
            return "Abajo"
        elif self ==  self.IZQUIERDA:
            return "Izquierda"
        elif self == self.DERECHA:
            return "Derecha"
        elif self == self.PUÑO:
            return "Puño"
        elif self == self.PATADA:
            return "Patada"
        elif self == self.TALADOKEN:
            return "Taladoken"
        elif self == self.TALADOKEN2:
            return "Taladoken"
        elif self == self.REMUYUKEN:
            return "Remuyuken"
        elif self == self.REMUYUKEN2:
            return "Remuyuken"
        else:
            raise Exception("Movimiento no valido")

    @classmethod

    def strtToAction(cls,string) -> 'Action':
        if string == "W":
            return cls.ARRIBA
        elif string == "S":
            return cls.ABAJO
        elif string == "A":
            return cls.IZQUIERDA
        elif string =="D":
            return cls.DERECHA
        elif string == "P":
            return cls.PUÑO
        elif string == "K":
            return cls.PATADA
        elif string == "DSDP":
            return cls.TALADOKEN
        elif string == "ASP":
            return cls.TALADOKEN2
        elif string == "DSDP":
            return cls.TALADOKN2
        elif string == "SAK":
            return cls.TALADOKEN2








