from plants import Plant
from interfaces import Identifiable, IHospitable

class BlueJadeVine:

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Partial", 0, "Medium" )
        Identifiable.__init__(self)
        IHospitable.__init__(self)
        self.hospitable_locations = set("Forest", "Swamp")