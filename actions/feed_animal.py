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
    for food in animal.prey:
        animal.feed(food)
    choice = input("> ")

    





