# wpe1_travel

from __future__ import print_function

places = dict()

while True:
    
    response = raw_input("Tell me where you went:")

    if len(response) == 0:
        break
    else:
        try:
            place = response.split(',')
            country = place[1]
            city = place[0]
            
            if country not in places:
                places[country] = [city]
            else:
                places[country].append(city)
                
        except:
            print("That's not a legal city, state combination")
    
data = dict()
# for every city in cities list for each country
# create dict of city along with the number of times
# the city appears
for country in places:
    cities = dict()
    for city in places[country]:
        if city not in cities:
            cities[city] = 1
        else:
            cities[city] += 1

    data[country] = cities


print("")
print("You visited")
countries = data.keys()
countries.sort()
for country in countries:
    print(country.strip())
    cities_dict = data[country]
    cities = cities_dict.keys()
    cities.sort()
    for city in cities:
        print(city,cities_dict[city])

