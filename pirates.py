command = input()
cities_dict = {}
while command != "Sail":
    city, populations, golds = command.split("||")
    populations, golds = int(populations), int(golds)
    if city not in cities_dict:
        cities_dict[city] = {"Population": 0, "Gold": 0}
    cities_dict[city]["Population"] += populations
    cities_dict[city]["Gold"] += golds
    command = input()
commands = input()
townes = []
while commands != "End":
    current_command = commands.split("=>")
    if current_command[0] == "Plunder":
        town, people, gold = current_command[1], int(current_command[2]), int(current_command[3])
        cities_dict[town]["Population"] -= people
        cities_dict[town]["Gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_dict[town]["Population"] <= 0 or cities_dict[town]["Gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            cities_dict.pop(town)

    elif current_command[0] == "Prosper":
        town, gold = current_command[1], int(current_command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[town]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town]['Gold']} gold.")
    commands = input()

if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for towns, population_gold in cities_dict.items():
        print(f"{towns} -> Population: {population_gold['Population']} citizens, Gold: {population_gold['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
