import os
from plants import BlueJadeVine, MountainAppleTree, Silversword, RainbowEucalyptusTree

def cultivate_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    plant = None
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus")
    print("4. Blue Jade Vine")
    print()
    print("Choose plant to cultivate.")
    choice = input("> ")

    if choice == "1":
        plant = MountainAppleTree()

    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = RainbowEucalyptusTree()
    
    if choice == "4":
        plant = BlueJadeVine()

    biome = dict()

    num = 1

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{num}. Mountain ({len(mountain.plants)} plants)')
        biome[num] = arboretum.mountains[index]
        num += 1

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{num}. Swamp ({len(swamp.plants)} plants)')
        biome[num] = arboretum.swamps[index]
        num += 1
    
    for index, grassland in enumerate(arboretum.grasslands):
        print(f'{num}. Grassland ({len(grassland.plants)} plants)')
        biome[num] = arboretum.grasslands[index]
        num += 1
    
    for index, forest in enumerate(arboretum.forests):
        print(f'{num}. Forest ({len(forest.plants)} plants)')
        biome[num] = arboretum.forests[index]
        num += 1
    
    
    print()
    print("Where would you like to place the plant?")
    choice = input("> ")

    try:
        env = biome[int(choice)]
        def choice_fn(environment):
            try:
                if environment.max_plants > len(environment.plants):
                    environment.add_plant(plant)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("**** That biome is not large enough ****")
                    print("**** Please choose another one ****")
                    print()
                    num = 1

                    for index, mountain in enumerate(arboretum.mountains):
                        print(f'{num}. Mountain ({len(mountain.plants)} plants)')
                        biome[num] = arboretum.mountains[index]
                        num += 1

                    for index, swamp in enumerate(arboretum.swamps):
                        print(f'{num}. Swamp ({len(swamp.plants)} plants)')
                        biome[num] = arboretum.swamps[index]
                        num += 1
                    
                    for index, grassland in enumerate(arboretum.grasslands):
                        print(f'{num}. Grassland ({len(grassland.plants)} plants)')
                        biome[num] = arboretum.grasslands[index]
                        num += 1
                    
                    for index, forest in enumerate(arboretum.forests):
                        print(f'{num}. Forest ({len(forest.plants)} plants)')
                        biome[num] = arboretum.forests[index]
                        num += 1
                    
                    
                    print()
                    print(f'Where would you like to release the {plant.species}?')
                    choice = input("> ")
                    env = biome[int(choice)]
                    choice_fn(env)
            except ValueError:
                pass
            except KeyError:
                pass
        
        choice_fn(env)
    except ValueError:
        pass
    except KeyError:
        pass
    