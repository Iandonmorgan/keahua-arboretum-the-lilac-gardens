
from animals import Animal
from interfaces import IFlying, IWalking, ISwimming, ITerrestrial, IEnviroChar

class NeneGoose(Animal, IFlying, IWalking, ISwimming, ITerrestrial, IEnviroChar):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IFlying.__init__(self)
        IWalking.__init__(self)
        ISwimming.__init__(self)
        ITerrestrial.__init__(self)
        IEnviroChar.__init__(self)
        self.__prey = { "Vegetation" }
        self.hospitable_rainfall.append("Little")
        self.hospitable_sunlight.append("Full")

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Nene Goose ate {prey} for a meal')
        else:
            print(f'The Nene Goose rejects the {prey}')

    def __str__(self):
        return f'Nene Goose ({str(self.id).split("-")[0]}). is Goosing around!'