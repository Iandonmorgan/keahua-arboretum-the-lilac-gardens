
from animals import Animal
from interfaces import Identifiable, ISwimming, ISaltwater, IHospitable

class Ulae(Animal, ISwimming, ISaltwater):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        self.__prey = {"Fish"}


    @property
    def prey(self):
        return self.__prey

    def __str__(self):
        return f'Ulae ({str(self.id).split("-")[0]}). is Ulaeing around!'
