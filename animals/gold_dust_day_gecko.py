from animals import Animal
from interfaces import Identifiable, IWalking, ITerrestrial, IHospitable, IEnviroChar

class GoldDustDayGecko(Animal,Identifiable, IWalking, ITerrestrial, IHospitable, IEnviroChar):

    def __init__(self):
        Animal.__init__(self, "River Gecko")
        IWalking.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        IHospitable.__init__(self)
        IEnviroChar.__init__(self)
        self.__prey = { "insects" }
        self.hospitable_locations.add("Forest")
        self.hospitable_altitude.append("Low")
        self.hospitable_rainfall.append("Rainy")
        self.hospitable_sunlight.append("Shady")

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Gecko ate {prey} for a meal')
        else:
            print(f'The Gecko rejects the {prey}')


    def __str__(self):
        return f'Gecko {self.id}. is Geckoing around!'
