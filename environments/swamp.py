import sys
sys.path.append('../')

from interfaces import IStagnant, Identifiable, IContainsAnimals, IContainsPlants


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.max_animals = 8
      self.max_plants = 12
      self.characteristics = "Stagnant fresh water"

    def add_animal(self, item):
        try:
            if self.max_animals > len(self.animals) and isinstance(item, IStagnant):
                self.animals.append(item)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-stagnant animals to a swamp")

    def add_plant(self, plant):
        try:
            for location in plant.hospitable_locations:
                if location == self:
                    if self.max_plants > len(self.plants):
                        self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants not hospitable for this environment.")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return self.name
