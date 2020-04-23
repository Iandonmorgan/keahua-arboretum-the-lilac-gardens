from plants import Plant
from interfaces import Identifiable, IHospitable

class RainbowEucalyptusTree:

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Shade", 8, "Low" )
        Identifiable.__init__(self)
        IHospitable.__init__(self)
        self.hospitable_locations = set("Forest")
        