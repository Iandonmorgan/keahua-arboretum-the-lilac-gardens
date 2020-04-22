class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__mountains = []
        self.__swamps = []
        self.__grasslands = []
        self.__forests = []
        self.__rivers = []

    @property
    def mountains(self):
        return self.__mountains

    def annex_mountain(self, mountain):
        self.__mountains.append(mountain)

    @property
    def swamps(self):
        return self.__swamps

    def annex_swamp(self, swamp):
        self.__swamps.append(swamp)

    @property
    def grasslands(self):
        return self.__grasslands

    def annex_grassland(self, grassland):
        self.__grasslands.append(grassland)

    @property
    def forests(self):
        return self.__forests

    def annex_forest(self, forest):
        self.__forests.append(forest)

    @property
    def rivers(self):
        return self.__rivers

    def annex_river(self, river):
        self.__rivers.append(river)