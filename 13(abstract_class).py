# it is used to inforce rule rule to declear some method on other child class
from abc import ABC, abstractmethod


class shapes(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class rectangle(shapes):
   def __init__(self, alength, abredth):
     self.length = alength
     self.bredth = abredth
   def printarea(self):
     return self.length * self.bredth



rect = rectangle(45, 45)

print(rect.printarea())

    