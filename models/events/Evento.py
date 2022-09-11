import abc 


class Event(metaclass=abc.ABCMeta):

    @abc.abstractmethod

    def startEvent(self):
        pass
        