from models.movements.Movement import Movement



class Taladoken(Movement):


    def getComand(self) -> str:

        return "DSDP"


    def getEnergyPoints(self) -> int:

        return 3

    def __str__(self) -> str:

        return "Taladoken"

