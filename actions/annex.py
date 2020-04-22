import os
from environments import Mountain, Swamp, Grassland, Forest, River

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("")
    print("Choose what you want to annex.")
    choice = input("> ")

    if choice == "1":
        mountain = Mountain()
        arboretum.mountains.append(mountain)
    if choice == "2":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
    if choice == "3":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
    if choice == "4":
        forest = Forest()
        arboretum.forests.append(forest)
    if choice == "5":
        river = River()
        arboretum.rivers.append(river)

