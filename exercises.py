# Exercise 0
# Lists
fav_colors = ["Truqoise", "Electric Orange", "Cool blue", "Navy", "Yellow"]
ages = [25, 31, 24, 23, 22, 26]
coin_flips = [True, False, True, True, False] # True indicating that it was heads
fav_artists = ["Post Malone", "Billie Eilish", "Joji"]

# Dictionaries
words = {"Sardonic" : "Mocking and Cynical", "Contingency" : "Preparing for unforseen circumstance", "Peruse" : "Read thoroughly"}
fav_movies = {"Terminator 2" : 1991, "Lala Land" : 2016, "Spiderman Into the Spiderverse" : 2018}
cities = {"Hong Kong" : 7392000, "Toronto" : 2930000, "New York" : 8623000}
family_and_freinds = {"Sharon" : 31, "Moo Moo" : 22, "Aj" : 24, "Ian" : 24, "Keefe" : 42, "Kat" : 40}

#########################
# Exercise 1

# 1.1
for coin in coin_flips:
    print(coin)

# 1.2
print(fav_colors[0])

# 1.3
ages.sort() # sort does not return a value, thats why print(age.sort() doesn't work)
print(ages)

# 1.4
ages.append(0)
print(ages)

# 1.5
print(fav_movies["Terminator 2"])

###########################
# Exercise 2

# 2.1
print(fav_colors[-1])

# 2.2
cities["San Francisco"] = 884363
# Checking to see if it was added successfully
for city, pop in cities.items():
    print(f"{city} has a population of {pop}")

# 2.3
coin_flips.reverse() # Don't need to call to variable, reverse() just reverses and saves the variable
print(coin_flips) # Checking to see if it was reversed

# 2.4
print(cities["Hong Kong"])

# 2.5
for artist in fav_artists:
    print(f"I think {artist} is great")

############################
# Exercise 3

# 3.1
print(fav_artists[0:2])

# 3.2
for movie, year in fav_movies.items():
    print(f"{movie} came out {year}")

# 3.3
ages = sorted(ages, reverse = False)
print(ages)

# 3.4
fav_movies["Beauty and the Beast"] = [1991, 2017]
print(fav_movies["Beauty and the Beast"])

##############################
# Exercise 4

# 4.1
under_30 = list(filter(lambda age: age < 30, ages))
print(under_30)

# 4.2
print(max(ages))

# 4.3
print(coin_flips.count(True))

# 4.4
fav_artists.remove("Joji")
print(fav_artists)

# 4.5
cities["Toronto"] = 2930001
print(cities["Toronto"])

###############################
# Exercise 5

# 5.1
total_pop = 0
for pop in cities.values():
    total_pop += pop
print(total_pop)

# 5.2
for member, age in family_and_freinds.items():
    if age < 32:
        print(f"{member} is young")
    else:
        print(f"{member} is old")

# 5.3
print(fav_colors[-2:])

# 5.4
print(ages) # Printing original to make it easier to see if adding one to ages is implemented correctly
ages = list(map(lambda age: age + 1, ages))
print(ages)

# 5.5
fav_colors.append("Sea Green")
fav_colors.append("Coral Blue")
print(fav_colors)

###############################
# Exercise 6

# 6.1
movies = {1999 : ["The Matrix", "Star Wars Ep 1", "The Mummy"], 2009 : ["Avatar", "Star Trek", "District 9"], 2019: ["How to Train Your Dragon 3", "Tory Story 4", "Star Wars Episode 9"]}

# 6.2
phone_buttons = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

# 6.3
countries = [{"Canada" : {"Continent" : "North America", "Island" : False}}, {"America" : {"Continent" : "North America", "Island" : False}}, {"Japan" : {"Continent" : "Asia", "Island" : True}}]

################################
# Exercise 7

# 7.1
for i in range(20):
    print("I will not skateboard in the halls")

# 7.1
skateboard_message = []
for i in range(20):
    skateboard_message.append("I will not skateboard in the halls")
print(len(skateboard_message)) # Shows length of the list. It should show 20

# 7.2
fifty_list = []
for i in range(50):
    fifty_list.append(i+1)
print(fifty_list) # Checking to see if it was added correctly

# 7.3
total = 0
for num in fifty_list:
    total += num
print(total)

# 7.4
triple_fifty = []
for i in range(50):
    triple_fifty.append(i+1)
    triple_fifty.append(i+1)
    triple_fifty.append(i+1)
print(triple_fifty)

# 7.5
not_island = []
for country in countries:
    for characteristics in country.values():
        if characteristics["Island"] == True:
            not_island.append(country)
print(countries)
print(not_island)

###################################
# Exercise 8

def sum_expenses(yearly_expense):
    total_expense = 0
    for expense in yearly_expense:
        total_expense += expense
    return total_expense

year1 = [92, 25, 83, 15, 67]
year2 = [100, 29, 58, 47, 12, 39, 28]

print(sum_expenses(year1))
print(sum_expenses(year2))

