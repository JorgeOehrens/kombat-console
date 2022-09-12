from models.movements.Movement import Movement



class Puño(Movement):


    def getComand(self) -> str:

        return "P"


    def getEnergyPoints(self) -> int:

        return 1

    def __str__(self) -> str:

        return "Puño"



class Patada(Movement):



    def getComand(self) -> str:

        return "K"


    def getEnergyPoints(self) -> int:

        return 1

    def __str__(self) -> str:

        return "Patada"



class Arriba(Movement):



    def getComand(self) -> str:

        return "W"


    def getEnergyPoints(self) -> int:

        return 0

    def __str__(self) -> str:

        return "Arriba"


class Abajo(Movement):



    def getComand(self) -> str:

        return "S"


    def getEnergyPoints(self) -> int:

        return 0

    def __str__(self) -> str:

        return "Abajo"


class Izquierda(Movement):



    def getComand(self) -> str:

        return "A"


    def getEnergyPoints(self) -> int:

        return 0

    def __str__(self) -> str:

        return "Izquierda"


class Derecha(Movement):
    
        def getComand(self) -> str:
    
            return "D"
    
    
        def getEnergyPoints(self) -> int:
    
            return 0
    
        def __str__(self) -> str:
    
            return "Derecha"


