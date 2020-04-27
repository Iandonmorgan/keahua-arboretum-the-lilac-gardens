from interfaces import Identifiable

class Animal(Identifiable):

    def __init__(self, species):
        self.species = species
        self.minimum_age_months = 0
        Identifiable.__init__(self)

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
