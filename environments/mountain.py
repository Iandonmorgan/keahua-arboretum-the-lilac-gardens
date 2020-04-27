from interfaces import Identifiable, IContainsAnimals, IContainsPlants

class Mountain(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.max_animals = 6
      self.max_plants = 4
      self.characteristics: "High Elevation"

    def add_animal(self, animal):
        if "High Elevation" not in animal.hospitable_altitude:
            print()
            print(f'Mountain environment is not hospitable for {animal.species}.')
            input("Press any key to return to main menu...")
        else:
            self.animals.append(animal)
            print()
            print(f'{animal.species} added to Mountain environment.')
            input("Press any key to return to main menu...")
        
    def add_plant(self, plant):
        if "Mountain" not in plant.hospitable_locations:
            print()
            print(f'Mountain environment is not hospitable for {plant.species}.')
            input("Press any key to return to main menu...")
        else:
            self.plants.append(plant)
            print()
            print(f'{plant.species} added to Mountain environment.')
            input("Press any key to return to main menu...")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'