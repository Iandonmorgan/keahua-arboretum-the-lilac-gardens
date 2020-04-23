
from animals import Animal
from interfaces import Identifiable, IFlying, IWalking, ISwimming, ITerrestrial, IHospitable

class NeneGoose(Animal, Identifiable, IFlying, IWalking, ISwimming, ITerrestrial, IHospitable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IWalking.__init__(self)
        ISwimming.__init__(self)
        ITerrestrial.__init__(self)
        IHospitable.__init__(self)
        self.__prey = { "Vegetation" }



    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Nene Goose ate {prey} for a meal')
        else:
            print(f'The Nene Goose rejects the {prey}')

    def __str__(self):
        return f'Nene Goose {self.id}. is Goosing around!'