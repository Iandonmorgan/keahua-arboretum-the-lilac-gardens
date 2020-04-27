import os
from interfaces import Identifiable, IContainsAnimals, IContainsPlants


class Volcano(IContainsAnimals, IContainsPlants, Identifiable):
    
    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = "Volcano"
        self.max_animals = 999999999999999

    def add_animal(self, item):
        self.animals.append(item)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
                                              ooO
                             ooOOOo
                           oOOOOOOoooo
                         ooOOOooo  oooo
                        /vvv\\
                       /V V V\ 
                      /V  V  V\          
                     /         \          GODDESS PELE IS PLEASED!
                    /           \               /
                  /               \   	  o          o
        __       /                 \     /-   o     /-
        /\     /                     \  /\  -/-    /\\
                                            /\\
        {item.species} sacrificed to Goddess Pele.
        """)
        input("Press any key to return to main menu...")

    def add_plant(self, item):
        self.animals.append(item)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
                                              ooO
                             ooOOOo
                           oOOOOOOoooo
                         ooOOOooo  oooo
                        /vvv\\
                       /V V V\ 
                      /V  V  V\          
                     /         \          I HOPE GODDESS PELE IS VEGAN!
                    /           \               /
                  /               \   	  o          o
        __       /                 \     /-   o     /-
        /\     /                     \  /\  -/-    /\\
                                            /\\
        {item.species} sacrificed to Goddess Pele.
        """)
        input("Press any key to return to main menu...")