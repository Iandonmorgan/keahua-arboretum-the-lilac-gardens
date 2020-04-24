from animals import Animal
from interfaces import Identifiable, ISwimming, ISaltwater, IHospitable

class Kikapu(Animal, Identifiable, ISwimming, ISaltwater, IHospitable):

    def __init__(self):
        Animal.__init__(self, "Kikapu")
        ISaltwater.__init__(self)
        ISwimming.__init__(self)
        Identifiable.__init__(self)
        IHospitable.__init__(self)
        self.__prey = { "fish" }
  

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kikapu ate {prey} for a meal')
        else:
            print(f'The Kikapu rejects the {prey}')


    def __str__(self):
        return f'Kikapu ({str(self.id).split("-")[0]}). is Kikapuing around!'
