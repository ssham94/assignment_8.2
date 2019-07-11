# Exercise 0
# Lists
fav_colors = ["Truqoise", "Electric Orange", "Cool blue", "Navy", "Yellow"]
age = [25, 31, 24, 23, 22, 26]
coin_flips = [True, False, True, True, False] # True indicating that it was heads
fav_artists = ["Post Malone", "Billie Eilish", "Joji"]

# Dictionaries
words = {"Sardonic" : "Mocking and Cynical", "Contingency" : "Preparing for unforseen circumstance", "Peruse" : "Read thoroughly"}
fav_movies = {"Terminator 2" : 1991, "Lala Land" : 2016, "Spiderman Into the Spiderverse" : 2018}
cities = {"Hong Kong" : 7392000, "Toronto" : 2930000, "New York" : 8623000}
family_and_freinds = {"Sharon" : 31, "Moo Moo" : 22, "Aj" : 24, "Ian" : 24}

#########################
# Exercise 1

# 1.1
for coin in coin_flips:
    print(coin)

# 1.2
print(fav_colors[0])

# 1.3
age.sort() # sort does not return a value, thats why print(age.sort() doesn't work)
print(age)

# 1.4
age.append(0)
print(age)

# 1.5
print(fav_movies["Terminator 2"])

