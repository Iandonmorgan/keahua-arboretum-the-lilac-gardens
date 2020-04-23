import os
from animals import RiverDolphin, GoldDustDayGecko, NeneGoose, Kikapu, Pueo, Ulae, Opeapea, HappyFaceSpider

def feed_animal_menu(arboretum):
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
    print("Choose an animal to feed.")
    choice = input("> ")

    if choice == "1":
        animal = GoldDustDayGecko()
        feed_animal(animal)
    if choice == "2":
        animal = RiverDolphin()
        feed_animal(animal)
    if choice == "3":
        animal = NeneGoose()
        feed_animal(animal)
    if choice == "4":
        animal = Kikapu()
        feed_animal(animal)
    if choice == "5":
        animal = Pueo()
        feed_animal(animal)
    if choice == "6":
        animal = Ulae()
        feed_animal(animal)
    if choice == "7":
        animal = Opeapea()
        feed_animal(animal)
    if choice == "8":
        animal = HappyFaceSpider()
        feed_animal(animal)

def feed_animal(animal):
    os.system('cls' if os.name == 'nt' else 'clear')
    num = 1

    animalPreyToList = list(animal.prey)
    for food in animalPreyToList:
        print(f"{num} {food}")
        num += 1
    
    print()
    choice1 = input(f"What would you like to feed the {animal.species}? ")
    print()
    prey_index = int(choice1) - 1
    
    os.system('cls' if os.name == 'nt' else 'clear')
    animal.feed(animalPreyToList[prey_index])
    print()
    choice2 = input("Press any key to return to main menu... ")







