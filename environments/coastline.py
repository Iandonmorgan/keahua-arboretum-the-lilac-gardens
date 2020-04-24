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
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or freshwater animals to a coastline environment.")

    def add_plant(self, plant):
        try:
            for location in plant.hospitable_locations:
                if location == self:
                    if self.max_plants > len(self.plants):
                        self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants not hospitable for this environment.")

    def animal_count(self):
        return f'This place has {len(self.animals)} animals in it'

    def __str__(self):
        return f'{self.name}({str(self.id).split("-")[0]})'