from animals import Animal
from interfaces import IWalking, ITerrestrial, IEnviroChar

class GoldDustDayGecko(Animal, IWalking, ITerrestrial, IEnviroChar):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        IWalking.__init__(self)
        ITerrestrial.__init__(self)
        IEnviroChar.__init__(self)
        self.__prey = { "insects" }
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
        return f'Gecko ({str(self.id).split("-")[0]}). is Geckoing around!'
