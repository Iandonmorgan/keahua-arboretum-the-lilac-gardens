from plants import Plant
from interfaces import Identifiable, IHospitable

class MountainAppleTree:

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Partial", 17, "High" )
        Identifiable.__init__(self)
        IHospitable.__init__(self)
        self.hospitable_locations = ["Mountain"]