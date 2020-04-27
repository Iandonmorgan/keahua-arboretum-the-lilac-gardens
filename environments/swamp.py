from interfaces import IStagnant, Identifiable, IContainsAnimals, IContainsPlants


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.max_animals = 8
      self.max_plants = 12
      self.characteristics = "Stagnant fresh water"

    def add_animal(self, animal):
            if isinstance(animal, IStagnant):
                self.animals.append(animal)
                print()
                print(f'Swamp environment is not hospitable for {animal.species}.')
                input("Press any key to return to main menu...")
            else:
                print()
                print(f'Swamp environment is not hospitable for {animal.species}.')
                input("Press any key to return to main menu...")

    def add_plant(self, plant):
        if "Swamp" not in plant.hospitable_locations:
            print()
            print(f'Swamp environment is not hospitable for {plant.species}.')
            input("Press any key to return to main menu...")
        else:
            self.plants.append(plant)
            print()
            print(f'{plant.species} added to Swamp environment.')
            input("Press any key to return to main menu...")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'
