from plants import Plant
from interfaces import Identifiable, IHospitable

class Silversword:

    def __init__(self):
        Plant.__init__(self, "Silversword", "Full", 22, "High" )
        Identifiable.__init__(self)
        IHospitable.__init__(self)
        self.hospitable_locations = set("Grassland")