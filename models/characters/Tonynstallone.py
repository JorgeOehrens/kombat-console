from models.characters.Character import Character
from models.movements.Taladoken import Taladoken



class   TonynStallone(Character):

    def __init__(self):
        super().__init__("Tony n' Stallone", 100)
        self.movements.append(Taladoken())


