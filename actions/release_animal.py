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

    # else:
    #      print("thats wrong")
    #      return

    

    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{index + 1}. Mountain {mountain.id}')

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{index + 1}. Mountain {mountain.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].add_animals(animal)
    arboretum.rivers[int(choice) - 1].add_animals(animal)
    arboretum.rivers[int(choice) - 1].add_animals(animal)
    arboretum.rivers[int(choice) - 1].add_animals(animal)
    
