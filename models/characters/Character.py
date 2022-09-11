import abc

from models.movements.Movement import Movement
from models.events.Event import Event
from rx.subject import Subject
from models.events.CharacterDie import CharacterDie

class Character(metaclass=abc.ABCMeta):
    def __init__(self, name: str, energy: int, movement : 'Movement') -> None:
        self.name = name
        self.energy = energy
        self.energyNow= energy
        self.movements = [movement]
        self.eventNow: Subject['Event'] = Subject()

    
    def getAttackEnergyPoints(self) -> int:
        return self.movements[0].getAttackEnergyPoints()
    

    def getDanage(self, character: 'Character') -> None:
        
        self.energyNow -= character.getAttackEnergyPoints()

        if self.energyNow < 0:
            self.energyNow = 0
            self.die()

    def attack(self, character: 'Character') -> None:
        character.getDanage(self)
    

    def die(self) -> None:
        self.eventNow.on_next(CharacterDie())
        self.eventNow.on_completed()