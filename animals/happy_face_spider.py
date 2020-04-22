from animals import Animal
from interfaces import Identifiable, IWalking, ITerrestrial

class HappyFaceSpider(Animal,Identifiable, IWalking, ITerrestrial):

    def __init__(self):
        Animal.__init__(self, "Happy Face Spider")
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
            print(f'The Happy Face Spider ate {prey} for a meal')
        else:
            print(f'The Happy Face Spider rejects the {prey}')


    def __str__(self):
        return f'Happy Face Spider {self.id}. is Happy Face Spidering around!'
