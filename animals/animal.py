class Animal:

    def __init__(self, species):
        self.species = species
        self.minimum_age_months = 0

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
