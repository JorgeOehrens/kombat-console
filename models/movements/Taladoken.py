from models.movements.Movement import Movement



class Taladoken(Movement):

    def getEnergyPoints(self) -> int:

        return 3

    def __str__(self) -> str:

        return "Taladoken"

