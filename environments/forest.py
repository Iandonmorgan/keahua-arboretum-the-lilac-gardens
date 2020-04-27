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
        if "Shady" in animal.hospitable_sunlight and "Rainy" in animal.hospitable_rainfall:
            self.animals.append(animal)
            print()
            print(f'{animal.species} added to Forest environment.')
            input("Press any key to return to main menu...")
        else:
            print()
            print(f'Forest environment is not hospitable for {animal.species}.')
            input("Press any key to return to main menu...")


    def add_plant(self, plant):
        if "Forest" not in plant.hospitable_locations:
            print()
            print(f'Forest environment is not hospitable for {plant.species}.')
            input("Press any key to return to main menu...")
        else:
            self.plants.append(plant)
            print()
            print(f'{plant.species} added to Forest environment.')
            input("Press any key to return to main menu...")


    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'


    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'