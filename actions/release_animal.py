import os

from animals import RiverDolphin, GoldDustDayGecko, NeneGoose, Kikapu, Pueo, Ulae, Opeapea, HappyFaceSpider

def release_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    animal = None
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    print()
    print("Choose animal.")
    choice = input("> ")

    if choice == "1":
        animal = GoldDustDayGecko()

    if choice == "2":
        animal = RiverDolphin()
        print(animal)

    if choice == "3":
        animal = NeneGoose()
    
    if choice == "4":
        animal = Kikapu()
    
    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Opeapea()

    if choice == "8":
        animal = HappyFaceSpider()
    

    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {len(river.animals)} animals')


    for index, mountain in enumerate(arboretum.mountains):
        print(f'{index + 1}. Mountain {len(mountain.animals)} animals')

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{index + 1}. Swamp {len(swamp.animals)} animals')
    
    for index, grassland in enumerate(arboretum.grasslands):
        print(f'{index + 1}. Grassland {len(grassland.animals)} animals')
    
    for index, forest in enumerate(arboretum.forests):
        print(f'{index + 1}. Forest {len(forest.animals)} animals')
    
    for index, coastline in enumerate(arboretum.coastlines):
        print(f'{index + 1}. Coastline {len(coastline.animals)} animals')
    
    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].add_animal(animal)
    arboretum.mountains[int(choice) - 1].add_animal(animal)
    arboretum.grasslands[int(choice) - 1].add_animal(animal)
    arboretum.forests[int(choice) - 1].add_animal(animal)
    arboretum.swamps[int(choice) - 1].add_animal(animal)
    arboretum.coastlines[int(choice) - 1].add_animal(animal)
    
