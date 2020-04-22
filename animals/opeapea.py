from animals import Animal
from interfaces import Identifiable, IFlying, IHospitable 

class Opeapea(Animal, Identifiable, IFlying, IHospitable):

    def __init__(self):
        Animal.__init__(self, "Opeapea")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IHospitable.__init__(self)
        self.__food = {"Insects and Vegetation"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Opeapea ate {prey} for a meal')
        else:
            print(f'The Opeapea rejects the {prey}')

    def __str__(self):
        return f'Nene Opeapea {self.id}. is Opapeaing around!'