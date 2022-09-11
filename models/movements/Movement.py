import abc 




class Movement(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod

    def getAttackEnergyPoints(self) -> int:
            pass
    
    @abc.abstractmethod

    def __str__(self) -> str:
            pass

