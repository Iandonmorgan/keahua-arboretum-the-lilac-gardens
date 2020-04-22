from animals import Animal
from interfaces import Identifiable, IFreshwater, ISwimming, IHospitable

class RiverDolphin(Animal, Identifiable, IFreshwater, ISwimming, IHospitable):

    def __init__(self):
        Animal.__init__(self, "River Dolphin")
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
        Identifiable.__init__(self)
        IHospitable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }



    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The River Dolphin ate {prey} for a meal')
        else:
            print(f'The River Dolphin rejects the {prey}')


    def __str__(self):
        return f'River Dolphin {self.id}. is River Dolphining around!'
