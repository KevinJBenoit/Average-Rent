
import housing_scrape
from housing_classes import City
import functions_module
import pickle


location = input("Please enter the zipcode or city and state you wish to search: (example: Colorado Springs, CO) \n")
is_zipcode = functions_module.zipcode_validate(location)

if is_zipcode:
    #call the web scraper
    average_price, location_type = housing_scrape.scrape_rent(location)

    #get the city, state from the zipcode
    city = functions_module.zipcode_lookup(location)

    #parse the name, and get the full state name and full city name assigned, can be refactored
    city_parse = city.split(',')
    state = functions_module.stateUnabbreviate(city_parse[1].strip())
    city_name = city_parse[0]

    #create a city with the appropriate zipcode
    city1 = City(city_name, state)
    city1.zipcodes.update({location: average_price}) #update the dictionary with a key value pair {zipcode : price}
    city1.city_update() #a new value was added, update the latest date/time


#else not a zipcode but a city and state
else:
    #call web scraper
    average_price, location_type = housing_scrape.scrape_rent(location)

    #parse the name, and get the full state name and full city name assigned
    city_parse = location.split(',')
    state = functions_module.stateUnabbreviate(city_parse[1].strip())
    city_name = city_parse[0]

    city1 = City(city_name, state)
    #if user wanted houses search, update the housing member
    if location_type == "-houses":
        city1.average_houses = average_price
    #else the user wanted apartments, update the apartment member
    else:
        city1.average_apartments = average_price
    city1.city_update()



try:
    with open("cities.pickle", "rb") as file:
        all_cities = pickle.load(file)
except IOError:
        all_cities = []
        with open("cities.pickle", "wb") as file:
            pickle.dump(all_cities, file)

for data_city in all_cities:
    #if the city is already present, replace the prices, update, and compare zipcodes
    if data_city.name == city1.name and city.state == city1.state:
        data_city.average_apartments = city1.average_apartments
        data_city.average_houses = city1.average_houses
        data_city.last_update = city1.last_update
        
        #if the zipcode from user is already in the data file, replace the price from the data file with the one from the user
        if city1.zipcodes[0] in data_city.zipcodes:
            data_city.zipcodes[city1.zipcodes[0]] = city1.zipcodes.get(city1.zipcodes[0])

        #else apppend the zipcode to the data file
        else:
            data_city.zipcodes = city1.zipcodes

    #else append the city info into the data file
    else:
        all_cities.append(city1)

#write the data to the pickle file
with open("cities.pickle", "wb") as file:
    pickle.dump(all_cities, file)


print(city1)

#########################################################testing
with open("cities.pickle", "rb") as file:
        testing = pickle.load(file)

print(all_cities)
print(testing)