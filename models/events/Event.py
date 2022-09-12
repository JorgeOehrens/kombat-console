import abc
from controller.Game import *


class Event(metaclass=abc.ABCMeta):

    @abc.abstractmethod

    def visitGame(self, game: 'Game' ):
        pass
        