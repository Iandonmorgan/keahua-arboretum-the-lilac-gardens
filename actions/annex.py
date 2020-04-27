import os
from environments import Mountain, Swamp, Grassland, Forest, River, Coastline

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")
    print("")
    print("Choose what you want to annex.")
    choice = input("> ")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        mountain = Mountain()
        arboretum.mountains.append(mountain)
    elif choice == "2":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
    elif choice == "3":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
    elif choice == "4":
        forest = Forest()
        arboretum.forests.append(forest)
    elif choice == "5":
        river = River()
        arboretum.rivers.append(river)
    elif choice == "6":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
    else:
        input("That's not a valid option. Press any key to return to the main menu...")
