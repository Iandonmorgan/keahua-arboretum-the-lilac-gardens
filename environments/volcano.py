from interfaces import Identifiable, IContainsAnimals, IContainsPlants


class Volcano(IContainsAnimals, IContainsPlants, Identifiable):
    
    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = "Volcano"

    def add_animal(self, item):
        self.animals.append(item)
        print("feeed the volcano")