from animals import Animal
from interfaces import Identifiable, IWalking, ITerrestrial

class GoldDustDayGecko(Animal,Identifiable, IWalking, ITerrestrial):

    def __init__(self):
        Animal.__init__(self, "River Gecko")
        IWalking.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "insects" }
        self.hospitable_locations = list()


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
