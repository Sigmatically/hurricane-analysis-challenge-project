# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(costs):
    damages_float = []
    for cost in costs:
        if cost == "Damages not recorded":
            damages_float.append(cost)
        elif cost[-1].lower() == "m":
            damages_float.append(float(cost[:-1]) * 1000000)
        else:
            damages_float.append(float(cost[:-1]) * 1000000000)

    return damages_float

full_damage = update_damages(damages)

# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, full_damage, deaths):
    new_dict = {}
    for i in range(len(names)):
        new_dict[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": full_damage[i], "Deaths": deaths[i]}
    return new_dict

hurricane_name_dict = construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, full_damage, deaths)


# write your construct hurricane by year dictionary function here:
def hurricane_by_year(hurricane_dict):
    new_dict = {}
    for value in hurricane_dict.values():
        if value["Year"] in new_dict.keys():
            new_dict[value["Year"]].append(value)
        else:
            new_dict[value["Year"]] = [value]

    return new_dict

#print(hurricane_by_year(hurricane_name_dict))


# write your count affected areas function here:
def area_affect_count(areas):
    new_dict = {}
    for regions in areas:
        for region in regions:
            if region in new_dict.keys():
                new_dict[region] += 1
            else:
                new_dict[region] = 1
    return new_dict

area_affected_dict = area_affect_count(areas_affected)


# write your find most affected area function here:
def most_affected_area(area_dictionary):
    most_affected_key = list(area_dictionary.keys())[0]
    for key, value in area_dictionary.items():
        if value > area_dictionary[most_affected_key]:
            most_affected_key = key

    return most_affected_key, area_dictionary[most_affected_key]

print("{} was the most affected are by hurricanes hit approximately {} times".format(*most_affected_area(area_affected_dict)))

# write your greatest number of deaths function here:
def highest_deaths(hurricane_dict):
    current_highest_death = list(hurricane_dict.keys())[0]
    for key, value in hurricane_dict.items():
        if value["Deaths"] > hurricane_dict[current_highest_death]["Deaths"]:
            current_highest_death = key

    return current_highest_death, hurricane_dict[current_highest_death]["Deaths"]

print("{} had the highest number of deaths with a toll standing at {}".format(*highest_deaths(hurricane_name_dict)))


# write your catgeorize by mortality function here:
def mortality_rating(hurricane_dict):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    new_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for hurricane in hurricane_dict.values():
        if hurricane["Deaths"] >= 10000:
                new_dict[5].append(hurricane)
                continue
        for mortality, deaths in mortality_scale.items():
            if hurricane["Deaths"] <= deaths:
                new_dict[mortality].append(hurricane)
                break

    return new_dict

mortality_dict = mortality_rating(hurricane_name_dict)


# write your greatest damage function here:
def greatest_damage(hurricane_dict):
    greatest_damage = 0
    greatest_name = ""

    for name, hurricane in hurricane_dict.items():
        if hurricane["Damage"] == "Damages not recorded":
            continue
        elif hurricane["Damage"] > greatest_damage:
            greatest_damage = hurricane["Damage"]
            greatest_name = name
    
    return greatest_name, hurricane_dict[greatest_name]["Damage"]

print("Hurricane {} did the most damage causing ${} dollars in damage".format(*greatest_damage(hurricane_name_dict)))
print(hurricane_name_dict["Katrina"]["Damage"])

# write your catgeorize by damage function here:
def damage_rating(hurricane_dict):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    new_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for hurricane in hurricane_dict.values():
        if hurricane["Damage"] == "Damages not recorded":
            new_dict[0].append(hurricane)
            continue
        elif hurricane["Damage"] >= damage_scale[4]:
            new_dict[5].append(hurricane)
            continue
        
        for scale, damages in damage_scale.items():
            if hurricane["Damage"] <= damages:
                new_dict[scale].append(hurricane)
                break

    return new_dict

damages_dict = damage_rating(hurricane_name_dict)