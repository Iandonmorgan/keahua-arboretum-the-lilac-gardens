from plants import Plant

class Silversword(Plant):

    def __init__(self):
        Plant.__init__(self, "Silversword", "Full", 22, "High" )
        self.hospitable_locations = ["Grassland"]