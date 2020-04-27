import os
from plants import BlueJadeVine, MountainAppleTree, Silversword, RainbowEucalyptusTree

def cultivate_plant(arboretum):
    valid_option = True
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus")
    print("4. Blue Jade Vine")
    print()
    print("Choose plant to cultivate.")
    choice = input("> ")
    try:
        if int(choice) > 0 and int(choice) < 5:
            if choice == "1":
                plant = MountainAppleTree()

            if choice == "2":
                plant = Silversword()

            if choice == "3":
                plant = RainbowEucalyptusTree()
            
            if choice == "4":
                plant = BlueJadeVine()
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
            for index, mountain in enumerate(arboretum.mountains):
                if mountain.max_plants > len(mountain.plants):
                    print(f'{num}. Mountain ({len(mountain.plants)} plants)')
                    biome[num] = arboretum.mountains[index]
                    num += 1

            for index, swamp in enumerate(arboretum.swamps):
                if swamp.max_plants > len(swamp.plants):
                    print(f'{num}. Swamp ({len(swamp.plants)} plants)')
                    biome[num] = arboretum.swamps[index]
                    num += 1
            
            for index, grassland in enumerate(arboretum.grasslands):
                if grassland.max_plants > len(swamp.plants):
                    print(f'{num}. Grassland ({len(grassland.plants)} plants)')
                    biome[num] = arboretum.grasslands[index]
                    num += 1
            
            for index, forest in enumerate(arboretum.forests):
                if forest.max_plants > len(forest.plants):
                    print(f'{num}. Forest ({len(forest.plants)} plants)')
                    biome[num] = arboretum.forests[index]
                    num += 1
            
            for index, volcano in enumerate(arboretum.volcano):
                    print(f'{num}. Throw it in the volcano.')
                    biome[num] = arboretum.volcano[index]
                    num += 1
        except ValueError:
            print()
            error_message = input("Nope. Pick a number.")
        except KeyError:
            print()
            error_message = input("Nope. Pick a number.")
        except AttributeError:
            print()
            error_message = input("Nope. Pick a number.")
        except UnboundLocalError:
            error_message = input("Nope. Pick a number.")
    if valid_option and plant:
        menu_function()
        print()
        print("Where would you like to place the plant?")
        choice = input("> ")
    else:
        print()
        error_message = input("Hey, look. This is just irresponsible. Stop it.")


    try:
        env = biome[int(choice)]
        def choice_fn(environment):
            try:
                environment.add_plant(plant)
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                error_message = input("ValueError. Returning to main menu.")
            except KeyError:
                os.system('cls' if os.name == 'nt' else 'clear')
                error_message = input("Nope. Pick a number.")
            except AttributeError:
                os.system('cls' if os.name == 'nt' else 'clear')
                error_message = input("Nope. Pick a number.")
                pass
        
        choice_fn(env)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    except KeyError:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    except AttributeError:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    except UnboundLocalError:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    