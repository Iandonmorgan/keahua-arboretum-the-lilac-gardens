import os
from animals import RiverDolphin, GoldDustDayGecko, NeneGoose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider

def release_animal(arboretum):
    valid_option = True
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
    try:
        if int(choice) > 0 and int(choice) < 9:
            if choice == "1":
                animal = GoldDustDayGecko()

            if choice == "2":
                animal = RiverDolphin()

            if choice == "3":
                animal = NeneGoose()
            
            if choice == "4":
                animal = Kikakapu()
            
            if choice == "5":
                animal = Pueo()

            if choice == "6":
                animal = Ulae()

            if choice == "7":
                animal = Opeapea()

            if choice == "8":
                animal = HappyFaceSpider()
        else:
            pass
    except KeyError:
        os.system('cls' if os.name == 'nt' else 'clear')
        valid_option = False
        input("Please enter a valid option next time. Press enter to return to the main menu...")
    except AttributeError:
        os.system('cls' if os.name == 'nt' else 'clear')
        valid_option = False
        input("Please enter a valid option next time. Press enter to return to the main menu...")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        valid_option = False
        input("Please enter a valid option next time. Press enter to return to the main menu...")

    biome = dict()
    def menu_function():
        num = 1
        try:
            int(choice) == int
            if int(choice) > 0 and int(choice) < 9:
                for index, river in enumerate(arboretum.rivers):
                    if river.max_animals > len(river.animals):
                        print(f'{num}. River ({len(river.animals)} animals)')
                        biome[num] = arboretum.rivers[index]
                        num += 1

                for index, mountain in enumerate(arboretum.mountains):
                    if mountain.max_animals > len(mountain.animals):
                        print(f'{num}. Mountain ({len(mountain.animals)} animals)')
                        biome[num] = arboretum.mountains[index]
                        num += 1

                for index, swamp in enumerate(arboretum.swamps):
                    if swamp.max_animals > len(swamp.animals):
                        print(f'{num}. Swamp ({len(swamp.animals)} animals)')
                        biome[num] = arboretum.swamps[index]
                        num += 1
                
                for index, grassland in enumerate(arboretum.grasslands):
                    if grassland.max_animals > len(grassland.animals):
                        print(f'{num}. Grassland ({len(grassland.animals)} animals)')
                        biome[num] = arboretum.grasslands[index]
                        num += 1
                
                for index, forest in enumerate(arboretum.forests):
                    if forest.max_animals > len(forest.animals):
                        print(f'{num}. Forest ({len(forest.animals)} animals)')
                        biome[num] = arboretum.forests[index]
                        num += 1
                
                for index, coastline in enumerate(arboretum.coastlines):
                    if coastline.max_animals > len(coastline.animals):
                        print(f'{num}. Coastline ({len(coastline.animals)} animals)')
                        biome[num] = arboretum.coastlines[index]
                        num += 1

            for index, volcano in enumerate(arboretum.volcano):
                print(f'{num}. Throw it in the volcano.')
                biome[num] = arboretum.volcano[index]
                num += 1
                
        except KeyError:
            os.system('cls' if os.name == 'nt' else 'clear')
            input("Please enter a valid option next time. Press enter to return to the main menu...")
        except AttributeError:
            os.system('cls' if os.name == 'nt' else 'clear')
            input("Please enter a valid option next time. Press enter to return to the main menu...")
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            input("Please enter a valid option next time. Press enter to return to the main menu...")
    if valid_option:
        menu_function()
        print()
        print("Where would you like to place the animal?")
        choice = input("> ")

    try:
        env = biome[int(choice)]
        def choice_fn(environment):
            try:
                environment.add_animal(animal)
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                input("The environment is not suitable for that animal. Press any key to continue...")
                pass
            except KeyError:
                os.system('cls' if os.name == 'nt' else 'clear')
                input("The environment is not suitable for that animal. Press any key to continue...")
                pass
            except AttributeError:
                os.system('cls' if os.name == 'nt' else 'clear')
                input("The environment is not suitable for that animal. Press any key to continue...")
                pass
        
        choice_fn(env)
    except ValueError:
        pass
    except KeyError:
        pass
    except AttributeError:
        pass