from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Mountain(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.max_animals = 6
      self.max_plants = 4
      self.characteristics: "High Elevation"

    def add_animal(self, animal):
        try:
            for location in animal.hospitable_locations:
                if location == self:
                    self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add your animal to this non-hospitable environment.")

    def add_plant(self, plant):
        try:
            if self.max_plants > len(self.plants):
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("You got too many plants, fool!")
