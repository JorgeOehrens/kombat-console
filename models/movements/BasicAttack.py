from models.movements.Movement import Movement



class Puño(Movement):


    def getComand(self) -> str:

        return "P"


    def getAttackEnergyPoints(self) -> int:

        return 1

    def __str__(self) -> str:

        return "Puño"



class Patada(Movement):



    def getComand(self) -> str:

        return "K"


    def getAttackEnergyPoints(self) -> int:

        return 1

    def __str__(self) -> str:

        return "Patada"



class Arriba(Movement):



    def getComand(self) -> str:

        return "W"


    def getAttackEnergyPoints(self) -> int:

        return 0

    def __str__(self) -> str:

        return "Arriba"


class Abajo(Movement):



    def getComand(self) -> str:

        return "S"


    def getAttackEnergyPoints(self) -> int:

        return 0

    def __str__(self) -> str:

        return "Abajo"


class Izquierda(Movement):



    def getComand(self) -> str:

        return "A"


    def getAttackEnergyPoints(self) -> int:

        return 0

    def __str__(self) -> str:

        return "Izquierda"


class Derecha(Movement):
    
        def getComand(self) -> str:
    
            return "D"
    
    
        def getAttackEnergyPoints(self) -> int:
    
            return 0
    
        def __str__(self) -> str:
    
            return "Derecha"


