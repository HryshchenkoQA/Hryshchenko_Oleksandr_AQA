from abc import ABC
class Browser(ABC):
    _name = ''


    def __int__(self, history):
        self.__history = []

    @property
    def history(self):
        return self.__history