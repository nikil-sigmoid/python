countries = ["India", "France", "Russia"]
friend_countries = countries[:]

countries.append("USA")

friend_countries.append("UK")

print()
print("Printing original countries")
for country in countries:
    print(country)

print()
print("Printing friend countries")
for country in friend_countries:
    print(country)
