from models.movements.Movement import Movement



class Taladoken(Movement):


    def getComand(self) -> str:

        return "DSDP"


    def getAttackEnergyPoints(self) -> int:

        return 3

    def __str__(self) -> str:

        return "Taladoken"


class Taladoken2(Movement):


    def getComand(self) -> str:

        return "ASAP"


    def getAttackEnergyPoints(self) -> int:

        return 2

    def __str__(self) -> str:

        return "Taladoken"


class Remuyuken(Movement):


    def getComand(self) -> str:

        return "SDK"


    def getAttackEnergyPoints(self) -> int:

        return 2

    def __str__(self) -> str:

        return "Remuyuken"


class Remuyuken2(Movement):


    def getComand(self) -> str:

        return "SAK"


    def getAttackEnergyPoints(self) -> int:

        return 3

    def __str__(self) -> str:

        return "Remuyuken"

