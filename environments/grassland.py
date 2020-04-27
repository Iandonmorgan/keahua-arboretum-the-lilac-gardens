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
        if "Full" in animal.hospitable_sunlight and "Little" in animal.hospitable_rainfall:
            self.animals.append(animal)
            print()
            print(f'{animal.species} added to Grassland environment.')
            input("Press any key to return to main menu...")
        else:
            print()
            print(f'Grassland environment is not hospitable for {animal.species}.')
            input("Press any key to return to main menu...")

    def add_plant(self, plant):
        if "Grassland" not in plant.hospitable_locations:
            print()
            print(f'Grassland environment is not hospitable for {plant.species}.')
            input("Press any key to return to main menu...")
        else:
            self.plants.append(plant)
            print()
            print(f'{plant.species} added to Grassland environment.')
            input("Press any key to return to main menu...")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'
