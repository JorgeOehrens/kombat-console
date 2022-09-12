import abc

from models.movements.Movement import Movement
from models.events.Event import Event
from rx.subject import Subject
from models.events.CharacterDie import CharacterDie

class Character(metaclass=abc.ABCMeta):
    def __init__(self, name: str, energy: int, movements =[], specialAttack=[], basicAttack=[] ) -> None:
        self.name = name
        self.energy = energy
        self.energyNow= energy
        self.movements = []
        self.specialAttack = []
        self.basicAttack = []
        self.eventNow: Subject['Event'] = Subject() 

    
    def getAttackEnergyPoints(self,character: 'Character' ,movement: 'Movement') -> int:

        print(movement.getAttackEnergyPoints())
        return movement.getAttackEnergyPoints()

    def getDanage(self, character: 'Character', movement: 'Movement') -> None:
        
        self.energyNow -= character.getAttackEnergyPoints(character, movement)

        if self.energyNow < 0:
            self.energyNow = 0
            self.die()

    def attack(self, character: 'Character', movement: 'Movement') -> None:
        character.getDanage(self, movement)


    def die(self) -> None:
        self.eventNow.on_next(CharacterDie())
        self.eventNow.on_completed()