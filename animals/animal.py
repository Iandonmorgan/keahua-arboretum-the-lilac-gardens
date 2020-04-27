from interfaces import Identifiable

class Animal(Identifiable):

    def __init__(self, species):
        super().__init__()
        self.species = species
        self.minimum_age_months = 0

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
