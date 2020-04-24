import sys
from interfaces import Identifiable, IContainsAnimals, IContainsPlants

sys.path.append('../')

class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.max_animals = 22
      self.max_plants = 15
      self.characteristics: "Little rainfall, No shade"

    def add_animal(self, animal):
        try:
            for location in animal.hospitable_locations:
                if location == self:
                    self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add your animal to this non-hospitable environment.")

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