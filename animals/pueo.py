from animals import Animal
from interfaces import Identifiable, IFlying, IHospitable

class Pueo(Animal, Identifiable, IFlying, IHospitable):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IHospitable.__init__(self)
        self.__food = {"Rodents"}


    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Pueo ate {prey} for a meal')
        else:
            print(f'The Pueo rejects the {prey}')


    def __str__(self):
        return f'Pueo {self.id}. is Pueoing around!'