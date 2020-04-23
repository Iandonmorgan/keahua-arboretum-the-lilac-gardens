import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
from actions.feed_animal import feed_animal_menu

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

name_result = keahua.name
result = ""
for name in name_result:
    result = result + name + " "

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("|        ", result[:-1],"        |")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print()
    print("1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    print()
    print("Choose a KILLER option.")
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal_menu(keahua)

    if choice == "4":
        pass

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

main_menu()
