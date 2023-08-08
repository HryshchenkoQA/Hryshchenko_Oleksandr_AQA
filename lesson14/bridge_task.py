from abc import abstractmethod, ABC
class Road(ABC):
    def __init__(self, cover: int, lenght:int, bridge:int, crossroads:int ):
        self.cover = cover
        self.lenght = lenght
        self.bridge = bridge
        self.crossroads = crossroads

    @abstractmethod
    def add_bridge(self):
        pass


class Highway(Road):
    def __init__(self, cover: int, lenght:int, bridge:int, crossroads:int ):
        super().__init__(cover,lenght,bridge,crossroads)
        self.cover = 1

    def __prepare_for_bridge(self):
        print("Bridge are prepared")

    def __prepare_docs(self):
        print("all docs are ready")


    def add_bridge(self):
        self.__prepare_for_bridge()
        self.__prepare_docs()
        self.__finish()
        print("New bridge is ready. Number of bridges: " + self.bridge)
        return

    def __finish(self):
        self.bridge = +1
        print("bridge is ready")


class Dirty_road(Road):
    def __init__(self, cover: int, lenght:int, bridge:int, crossroads:int ):
        super().__init__(cover, lenght,bridge,crossroads)
        self.cover = 0

#oi blt