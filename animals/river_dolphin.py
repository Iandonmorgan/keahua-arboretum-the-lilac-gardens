from animals import Animal
from interfaces import IFreshwater, ISwimming

class RiverDolphin(Animal, IFreshwater, ISwimming):

    def __init__(self):
        Animal.__init__(self, "River Dolphin")
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
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
        return f'River Dolphin ({str(self.id).split("-")[0]}). is River Dolphining around!'
