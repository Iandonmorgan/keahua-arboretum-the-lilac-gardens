from interfaces import Identifiable, IHospitable

class Plant:

    def __init__(self, species, sunlight, seeds_produced, insecticide_resistance):
      Identifiable.__init__(self)
      IHospitable.__init__(self)
      self.species = species
      self.sunlight = sunlight
      self.seeds_produced = seeds_produced
      self.insecticide_resitance = insecticide_resistance


