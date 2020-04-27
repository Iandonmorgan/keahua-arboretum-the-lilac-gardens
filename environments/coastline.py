from interfaces import Identifiable, IContainsAnimals, IContainsPlants


class Coastline(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.max_animals = 15
      self.max_plants = 3
      self.characteristics = "Saltwater"

    def add_animal(self, animal):
        if animal.aquatic and animal.cell_type == "hypotonic":
            self.animals.append(animal)
            print()
            print(f'{animal.species} added to Coastline environment.')
            input("Press any key to return to main menu...")
        elif animal.species == "River Dolphin":
            self.animals.append(animal)
            print()
            print(f'{animal.species} added to Coastline environment.')
            input("Press any key to return to main menu...")
        else:
            print()
            print(f'Coastline environment is not hospitable for {animal.species}.')
            input("Press any key to return to main menu...")

    def add_plant(self, plant):
        if "Coastline" not in plant.hospitable_locations:
            print()
            print(f'Coastline environment is not hospitable for {plant.species}.')
            input("Press any key to return to main menu...")
        else:
            self.plants.append(plant)
            print()
            print(f'{plant.species} added to Coastline environment.')
            input("Press any key to return to main menu...")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'