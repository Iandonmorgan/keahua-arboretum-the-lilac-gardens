import os

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(arboretum.mountains) > 0:
        for mountain in arboretum.mountains:
            print(f'Mountain [{str(mountain.id).split("-")[0]}]')
            for animal in mountain.animals:
                print(f'    {animal.species} ({str(animal.id).split("-")[0]})')
            for plant in mountain.plants:
                print(f'    {plant.species} ({str(plant.id).split("-")[0]})')
        print()
    if len(arboretum.swamps) > 0:
        for swamp in arboretum.swamps:
            print(f'Swamp [{str(swamp.id).split("-")[0]}]')
            for animal in swamp.animals:
                print(f'    {animal.species} ({str(animal.id).split("-")[0]})')
            for plant in swamp.plants:
                print(f'    {plant.species} ({str(plant.id).split("-")[0]})')
        print()
    if len(arboretum.grasslands) > 0:
        for grassland in arboretum.grasslands:
            print(f'Grassland [{str(grassland.id).split("-")[0]}]')
            for animal in grassland.animals:
                print(f'    {animal.species} ({str(animal.id).split("-")[0]})')
            for plant in grassland.plants:
                print(f'    {plant.species} ({str(plant.id).split("-")[0]})')
        print()
    if len(arboretum.forests) > 0:
        for forest in arboretum.forests:
            print(f'Forest [{str(forest.id).split("-")[0]}]')
            for animal in forest.animals:
                print(f'    {animal.species} ({str(animal.id).split("-")[0]})')
            for plant in forest.plants:
                print(f'    {plant.species} ({str(plant.id).split("-")[0]})')
        print()
    if len(arboretum.rivers) > 0:
        for river in arboretum.rivers:
            print(f'River [{str(river.id).split("-")[0]}]')
            for animal in river.animals:
                print(f'    {animal.species} ({str(animal.id).split("-")[0]})')
            for plant in river.plants:
                print(f'    {plant.species} ({str(plant.id).split("-")[0]})')
        print()
    if len(arboretum.coastlines) > 0:
        for coastline in arboretum.coastlines:
            print(f'Coastline [{str(coastline.id).split("-")[0]}]')
            for animal in coastline.animals:
                print(f'    {animal.species} ({str(animal.id).split("-")[0]})')
            for plant in coastline.plants:
                print(f'    {plant.species} ({str(plant.id).split("-")[0]})')
        print()
    if len(arboretum.volcano) > 0:
        for volcano in arboretum.volcano:
            print(f'Offerings made to Pele [{str(volcano.id).split("-")[0]}]')
            for animal in volcano.animals:
                print(f'    {animal.species} ({str(animal.id).split("-")[0]})')
            for plant in volcano.plants:
                print(f'    {plant.species} ({str(plant.id).split("-")[0]})')

    input("\n\nPress any key to continue...")
