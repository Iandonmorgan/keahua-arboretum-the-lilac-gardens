from animals import Animal
from interfaces import ISwimming, ISaltwater

class Kikakapu(Animal, ISwimming, ISaltwater):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        ISaltwater.__init__(self)
        ISwimming.__init__(self)
        self.__prey = { "fish" }
  

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kīkākapu ate {prey} for a meal')
        else:
            print(f'The Kīkākapu rejects the {prey}')


    def __str__(self):
        return f'Kīkākapu ({str(self.id).split("-")[0]}). is Kīkākapuing around!'
