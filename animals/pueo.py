from animals import Animal
from interfaces import IFlying, IEnviroChar

class Pueo(Animal, IFlying, IEnviroChar):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        IFlying.__init__(self)
        IEnviroChar.__init__(self)
        self.__prey = {"Rodents"}
        self.hospitable_altitude.append("Low")
        self.hospitable_rainfall.append("Rainy")
        self.hospitable_rainfall.append("Little")
        self.hospitable_sunlight.append("Shady")
        self.hospitable_sunlight.append("Full")


    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Pueo ate {prey} for a meal')
        else:
            print(f'The Pueo rejects the {prey}')


    def __str__(self):
        return f'Pueo ({str(self.id).split("-")[0]}). is Pueoing around!'