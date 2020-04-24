from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Forest(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.max_animals = 20
      self.max_plants = 32
      self.characteristics: "Rainy, Shady"

    def add_animal(self, animal):
        try:
            for sunlight in animal.hospitable_sunlight:
                if sunlight == "Shady":
                    for rainfall in animal.hospitable_rainfall:
                        if rainfall == "Rainy":
                            self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add your animal to this non-hospitable environment.")

    def add_plant(self, plant):
        try:
            for location in plant.hospitable_locations:
                if location == "Forest":
                    if self.max_plants > len(self.plants):
                        self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants not hospitable for this environment.")


    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'


    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'