from interfaces import IAquatic, Identifiable, IContainsAnimals, IContainsPlants


class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.max_animals = 2
        self.max_plants = 6
        self.characteristics = "Fresh water"

    def add_animal(self, animal):
        if animal.aquatic and animal.cell_type == "hypertonic":
            self.animals.append(animal)
            print()
            print(f'{animal.species} added to River environment.')
            input("Press any key to return to main menu...")
        else:
            print()
            print(f'River environment is not hospitable for {animal.species}.')
            input("Press any key to return to main menu...") 

    def add_plant(self, plant):
        if "River" not in plant.hospitable_locations:
            print()
            print(f'River environment is not hospitable for {plant.species}.')
            input("Press any key to return to main menu...")
        else:
            self.plants.append(plant)
            print()
            print(f'{plant.species} added to River environment.')
            input("Press any key to return to main menu...")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'
