from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()
    @abstractmethod
    def move(self):
        pass


class Plane(Transport):
    def move(self):
        print('Летает по воздуху')
        

class Train(Transport):
    def move(self):
        print("Ездит по рельсам")


