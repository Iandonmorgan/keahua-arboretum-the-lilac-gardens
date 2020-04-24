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
            for altitude in animal.hospitable_altitude:
                if altitude == "High Elevation":
                    self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add your animal to this non-hospitable environment.")
        try:
            for location in animal.hospitable_locations:
                if location == self:
                    if self.max_animals > len(self.animals):
                        self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add your animal to this non-hospitable environment.")

    def add_plant(self, plant):
        try:
            for location in plant.hospitable_locations:
                if location == "Mountain":
                    if self.max_plants > len(self.plants):
                        self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants not hospitable for this environment.")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return self.name