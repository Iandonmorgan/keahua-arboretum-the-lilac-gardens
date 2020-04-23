from interfaces import IAquatic, Identifiable, IContainsAnimals, IContainsPlants


class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.max_animals = 12
        self.max_plants = 6
        self.characteristics = "Fresh water"

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                if self.max_animals > len(self.animals):
                    self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                if self.max_plants > len(self.plants):
                    self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return self.name
