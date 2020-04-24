from animals import Animal
from interfaces import Identifiable, IFlying, IHospitable,ITerrestrial, IEnviroChar 

class Opeapea(Animal, Identifiable, IFlying, IHospitable, ITerrestrial, IEnviroChar):

    def __init__(self):
        Animal.__init__(self, "Opeapea")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IHospitable.__init__(self)
        ITerrestrial.__init__(self)
        IEnviroChar.__init__(self)
        self.__prey = {"Insects and Vegetation"}
        self.hospitable_sunlight.append("Partial")
        self.hospitable_sunlight.append("Shade")
        self.hospitable_altitude.append("Low")
        self.hospitable_altitude.append("High Elevation")


    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Opeapea ate {prey} for a meal')
        else:
            print(f'The Opeapea rejects the {prey}')

    def __str__(self):
        return f'Nene Opeapea ({str(self.id).split("-")[0]}). is Opapeaing around!'