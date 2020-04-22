import sys
sys.path.append('../')

from interfaces import IStagnant
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    def __str__(self):
        return self.name
